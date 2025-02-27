from itertools import permutations, combinations

def palindromes_between_indices(s):
    s = s[1:7].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for combo in combinations(letters, length):
            for perm in permutations(combo):
                first_half = ''.join(perm[:length // 2])
                second_half = ''.join(perm[length // 2:])
                if length % 2 == 0:
                    palindrome = first_half + second_half[::-1]
                else:
                    middle_letter = perm[length // 2]
                    palindrome = first_half + middle_letter + second_half[::-1]
                palindromes.add(palindrome)
    return palindromes