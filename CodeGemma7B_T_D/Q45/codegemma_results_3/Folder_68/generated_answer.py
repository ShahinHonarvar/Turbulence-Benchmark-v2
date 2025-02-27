from itertools import permutations

def palindromes_between_indices(text):
    text = text[1:9].lower()
    result = set()
    for p in permutations(text):
        if len(''.join(p)) >= 4 and ''.join(p) == ''.join(p)[::-1]:
            result.add(''.join(p))
    return result