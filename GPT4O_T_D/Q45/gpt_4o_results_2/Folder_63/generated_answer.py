from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    sub_str = s[0:4].lower()
    letters = [char for char in sub_str if char.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in permutations(letters, r):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes