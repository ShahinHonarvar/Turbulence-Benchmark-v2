from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = ''.join([char.lower() for char in s[1:9] if char.isalpha()])
    palindromes = set()
    for i in range(4, len(substring) + 1):
        for perm in permutations(substring, i):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes