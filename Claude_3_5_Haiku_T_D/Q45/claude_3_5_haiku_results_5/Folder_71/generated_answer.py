from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[1:4] if c.isalpha()))
    result = set()

    def is_palindrome(word):
        return word == word[::-1]
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                result.add(candidate)
    return result