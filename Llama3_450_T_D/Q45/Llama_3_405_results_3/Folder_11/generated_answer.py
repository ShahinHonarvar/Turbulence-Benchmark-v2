from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:8] if c.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for perm in permutations(letters, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes