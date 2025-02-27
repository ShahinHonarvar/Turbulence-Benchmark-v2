from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[1:5])).lower()
    palindromes = set()
    n = len(letters)
    for i in range(2 ** n):
        combination = ''.join((letters[j] for j in range(n) if i & 1 << j))
        if len(combination) >= 5:
            for perm in set(permutations(combination)):
                pal = ''.join(perm)
                if is_palindrome(pal):
                    palindromes.add(pal)
    return palindromes