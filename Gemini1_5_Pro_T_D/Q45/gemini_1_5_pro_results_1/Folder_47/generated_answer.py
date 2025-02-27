from itertools import permutations

def palindromes_between_indices(text):
    result = set()
    for p in permutations(text[3:8].lower()):
        candidate = ''.join(p)
        if len(candidate) >= 5 and candidate == candidate[::-1]:
            result.add(candidate)
    return result