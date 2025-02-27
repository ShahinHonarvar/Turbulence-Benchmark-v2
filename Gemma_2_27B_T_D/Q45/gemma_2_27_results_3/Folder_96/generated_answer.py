from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:9].lower()
    letters = ''.join([c for c in substring if c.isalpha()])
    palindrome_set = set()
    for p in permutations(letters):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 6:
            palindrome_set.add(word)
    return palindrome_set