from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[5:7])).lower()
    if len(letters) < 2:
        return set()

    def is_palindrome(word):
        return word == word[::-1] and len(word) >= 3
    palindromes = set()
    for i in range(2, len(letters) + 1):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes