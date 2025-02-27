from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[3:6].lower()
    if len(s) < 3:
        return set()
    palindromes = set()
    letters = ''.join(filter(str.isalpha, s))
    if not letters:
        return set()
    for size in range(4, len(letters) + 1):
        for perm in permutations(letters, size):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes