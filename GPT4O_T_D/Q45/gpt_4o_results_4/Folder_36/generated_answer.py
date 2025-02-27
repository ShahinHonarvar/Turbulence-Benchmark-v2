from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substr = s[5:9].lower()
    letters = [c for c in substr if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                palindromes.add(perm_str)
    return palindromes