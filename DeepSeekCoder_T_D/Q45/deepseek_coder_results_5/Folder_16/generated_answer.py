from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[6:10])).lower()
    palindromes = set()
    n = len(letters)
    for i in range(2 ** n):
        combination = ''.join((letters[j] for j in range(n) if i & 1 << j))
        if len(combination) >= 5:
            for perm in set(permutations(combination)):
                word = ''.join(perm)
                if is_palindrome(word):
                    palindromes.add(word)
    return palindromes