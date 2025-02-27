from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[1:6].lower()))
    palindromes = set()
    for i in range(1, 1 << len(letters)):
        subset = ''.join((letters[j] for j in range(len(letters)) if i & 1 << j))
        if len(subset) >= 6:
            for perm in set(permutations(subset)):
                word = ''.join(perm)
                if is_palindrome(word):
                    palindromes.add(word)
    return palindromes