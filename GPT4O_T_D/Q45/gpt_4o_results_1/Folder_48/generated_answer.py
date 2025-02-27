import itertools

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    if len(s) < 9:
        return set()
    subset = s[6:9].lower()
    letters = ''.join(filter(str.isalpha, subset))
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for perm in itertools.permutations(letters, r):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes