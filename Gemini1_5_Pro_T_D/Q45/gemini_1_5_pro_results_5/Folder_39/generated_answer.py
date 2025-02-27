from itertools import permutations

def palindromes_between_indices(text):
    result = set()
    s = text[2:6]
    for i in range(3, len(s) + 1):
        for p in permutations(s, i):
            candidate = ''.join(p)
            if candidate.lower() == candidate[::-1].lower() and len(candidate) >= 3:
                result.add(candidate)
    return result