from itertools import permutations

def is_palindrome(word):
    return word == word[::-1]

def palindromes_between_indices(s):
    if len(s) < 7:
        return set()
    substr = s[5:7]
    chars = ''.join(filter(str.isalpha, substr)).lower()
    result = set()
    for i in range(3, len(chars) + 1):
        for p in permutations(chars, i):
            joined = ''.join(p)
            if is_palindrome(joined):
                result.add(joined)
    return result