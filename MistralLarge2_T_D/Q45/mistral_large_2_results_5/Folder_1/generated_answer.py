from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[4:8] if c.isalpha()]
    lower_letters = [c.lower() for c in letters]
    palindromes = set()
    for length in range(5, len(lower_letters) + 1):
        for perm in permutations(lower_letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes