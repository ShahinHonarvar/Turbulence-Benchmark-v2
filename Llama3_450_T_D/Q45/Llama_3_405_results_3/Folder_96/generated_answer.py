from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[3:9].lower() if c.isalpha()]
    if len(letters) < 6:
        return set()
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for perm in permutations(letters, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes