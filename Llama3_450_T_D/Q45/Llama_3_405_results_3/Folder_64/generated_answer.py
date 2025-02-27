from itertools import permutations

def palindromes_between_indices(s):
    english_letters = [c.lower() for c in s[4:10] if c.isalpha()]
    palindromes = set()
    for r in range(5, len(english_letters) + 1):
        for p in permutations(english_letters, r):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes