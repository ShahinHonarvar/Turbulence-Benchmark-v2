from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[0:7].lower()))
    palindromes = set()
    for i in range(2 ** len(letters)):
        combination = ''.join((c for j, c in enumerate(letters) if i & 1 << j))
        if len(combination) >= 6:
            for perm in set(permutations(combination)):
                word = ''.join(perm)
                if is_palindrome(word):
                    palindromes.add(word)
    return palindromes