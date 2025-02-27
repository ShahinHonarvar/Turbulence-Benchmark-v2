import itertools

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[4:7].lower()
    letters = ''.join(filter(str.isalpha, substring))
    permutations = set(itertools.permutations(letters))
    results = set()
    for perm in permutations:
        word = ''.join(perm)
        if len(word) >= 4 and is_palindrome(word):
            results.add(word)
    return results