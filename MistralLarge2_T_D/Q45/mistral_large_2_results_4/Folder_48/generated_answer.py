from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:9].lower()
    letters = [c for c in substring if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes