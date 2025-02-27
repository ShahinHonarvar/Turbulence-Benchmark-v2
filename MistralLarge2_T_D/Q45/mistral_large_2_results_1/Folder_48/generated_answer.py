from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    subset = s[6:9]
    english_letters = [c for c in subset if c.isalpha()]
    if len(english_letters) < 4:
        return set()
    palindromes = set()
    for length in range(4, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            word = ''.join(perm).lower()
            if is_palindrome(word) and word not in palindromes:
                palindromes.add(word)
    return palindromes