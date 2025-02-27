from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[1:5].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for i in range(5, len(s) + 1):
        for perm in permutations(s, i):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes