import re
    from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = re.sub('[^a-zA-Z]', '', s[1:5]).lower()
    all_permutations = set((''.join(p) for p in permutations(substring)))
    palindromes = {p for p in all_permutations if is_palindrome(p) and len(p) >= 5}
    return palindromes