from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    indices_range = s[3:8]
    letters = [c for c in indices_range if c.isalpha()]
    lowercase_letters = ''.join(letters).lower()
    if len(lowercase_letters) < 4:
        return set()
    palindromes = set()
    for length in range(4, len(lowercase_letters) + 1):
        for perm in permutations(lowercase_letters, length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes