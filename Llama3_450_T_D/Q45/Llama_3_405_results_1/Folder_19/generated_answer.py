from itertools import permutations

def palindromes_between_indices(s):
    english_letters = [c.lower() for c in s[1:8] if c.isalpha()]
    if len(english_letters) < 7:
        return set()
    palindromes = set()
    for r in range(7, len(english_letters) + 1):
        for perm in permutations(english_letters, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes