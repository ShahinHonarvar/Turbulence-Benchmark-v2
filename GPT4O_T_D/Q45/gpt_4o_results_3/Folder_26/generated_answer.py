from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    valid_chars = [c.lower() for c in s[4:7] if c.isalpha()]
    result = set()
    if len(valid_chars) < 3:
        return result
    for i in range(3, len(valid_chars) + 1):
        perm = permutations(valid_chars, i)
        for p in perm:
            word = ''.join(p)
            if is_palindrome(word):
                result.add(word)
    return result