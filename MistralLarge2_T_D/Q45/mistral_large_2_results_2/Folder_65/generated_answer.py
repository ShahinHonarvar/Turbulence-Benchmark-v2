from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:7]
    letters = [c for c in substring if c.isalpha()]
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            palindrome = ''.join(perm).lower()
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes