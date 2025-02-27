from itertools import permutations

def palindromes_between_indices(s):
    s = s[6:10].lower()
    if len(s) < 4:
        return set()

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters, 4):
        word = ''.join(perm)
        if is_palindrome(word):
            palindromes.add(word)
    return palindromes