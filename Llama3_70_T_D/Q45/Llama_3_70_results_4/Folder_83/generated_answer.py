from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for perm in permutations(letters, r):
            first_half = ''.join(perm[:r // 2])
            second_half = ''.join(perm[r // 2:]).rstrip(first_half[-1] if r % 2 == 0 else '')
            if first_half == second_half[::-1]:
                palindrome = first_half + (second_half if r % 2 == 0 else second_half + perm[r // 2]) + first_half[::-1]
                palindromes.add(palindrome)
    return palindromes