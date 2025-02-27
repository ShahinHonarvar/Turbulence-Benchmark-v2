from itertools import permutations
    import re

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = re.findall('[a-zA-Z]', s[:4])
    if len(letters) < 3:
        return set()
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p).lower()
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes