from itertools import permutations

def palindromes_between_indices(s):
    s_range = s[3:9].lower()
    letters_only = [c for c in s_range if c.isalpha()]
    palindromes_set = set()

    def is_palindrome(word):
        return word == word[::-1]
    for perm in permutations(letters_only, 6):
        if is_palindrome(perm):
            palindromes_set.add(''.join(perm))
    return palindromes_set