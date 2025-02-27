from itertools import permutations

def palindromes_between_indices(s):
    english_letters = [c for c in s[5:9] if c.isalpha()]
    letters = ''.join(english_letters).lower()
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in permutations(letters, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes