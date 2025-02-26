from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[4:10])).lower()
    palindromes = set()
    for i in range(7, len(letters) + 1):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes