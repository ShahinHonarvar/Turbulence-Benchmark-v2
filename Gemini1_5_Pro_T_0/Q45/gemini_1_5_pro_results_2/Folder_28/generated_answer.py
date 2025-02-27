from itertools import permutations

def palindromes_between_indices(text):
    result = set()
    for p in permutations(text[1:6]):
        candidate = ''.join(p)
        if len(candidate) >= 4 and candidate.lower() == candidate[::-1].lower():
            result.add(candidate.lower())
    return result