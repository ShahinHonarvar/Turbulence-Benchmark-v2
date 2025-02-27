from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substr = s[3:10].lower()
    letters = [c for c in substr if c.isalpha()]
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes