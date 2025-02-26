from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    letters = ''.join(filter(str.isalpha, s[7:10])).lower()
    if len(letters) < 2:
        return set()
    palindromes = set()
    for r in range(2, len(letters) + 1):
        for perm in permutations(letters, r):
            word = ''.join(perm)
            if len(word) >= 4 and is_palindrome(word):
                palindromes.add(word)
    return palindromes