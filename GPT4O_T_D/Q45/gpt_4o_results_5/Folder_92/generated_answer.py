from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    substring = s[4:8].lower()
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    if len(letters) < 4:
        return palindromes
    for r in range(4, len(letters) + 1):
        for perm in permutations(letters, r):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes