from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:8] if c.isalpha()]
    palindrome_set = set()
    for p in permutations(letters, len(letters)):
        word = ''.join(p)
        if word.lower() == word.lower()[::-1]:
            palindrome_set.add(word)
    return palindrome_set