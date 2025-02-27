from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    chars = [c.lower() for c in s[4:9] if c.isalpha()]
    if len(chars) < 6:
        return set()
    palindromes = set()
    for length in range(6, len(chars) + 1):
        for perm in permutations(chars, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes