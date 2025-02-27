from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    if len(s) < 4:
        return set()
    segment = s[1:4].lower()
    letters = [c for c in segment if c.isalpha()]
    result = set()
    for perm in permutations(letters):
        for length in range(4, len(letters) + 1):
            for start in range(0, len(perm) - length + 1):
                candidate = ''.join(perm[start:start + length])
                if is_palindrome(candidate):
                    result.add(candidate)
    return result