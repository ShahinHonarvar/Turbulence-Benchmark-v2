from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c.lower() for c in s[3:9] if c.isalpha()]
    result_set = set()
    for length in range(7, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for candidate in set((''.join(p) for p in list(perm) + list(perm)[::-1][1:])):
                if is_palindrome(candidate) and len(candidate) >= 7:
                    result_set.add(candidate)
    return result_set