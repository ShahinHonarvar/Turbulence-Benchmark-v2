from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:7])).lower()

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes