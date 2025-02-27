from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[1:6] if c.isalpha()]
    letters = [c.lower() for c in letters]
    unique_letters = set(letters)
    letters = list(unique_letters)
    palindromes = set()
    for r in range(2, len(letters) + 1):
        for perm in permutations(letters, r):
            palindrome = ''.join(perm) + ''.join(perm[::-1])
            if len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes