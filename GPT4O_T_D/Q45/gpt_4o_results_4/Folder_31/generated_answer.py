import itertools

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[1:9]
    english_letters = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for r in range(6, len(english_letters) + 1):
        for perm in itertools.permutations(english_letters, r):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes