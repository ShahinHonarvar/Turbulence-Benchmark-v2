from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[7:9]
    letters = [ch.lower() for ch in substring if ch.isalpha()]
    palindromes = set()
    if len(letters) < 3:
        return set()
    for i in range(3, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes