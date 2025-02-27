from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(text[1:4]).lower()
    result = set()
    for p in permutations(letters):
        s = ''.join(p)
        if s == s[::-1] and len(s) >= 4:
            result.add(s)
    return result