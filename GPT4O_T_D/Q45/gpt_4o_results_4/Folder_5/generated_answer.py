from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:9].lower()
    filtered_chars = ''.join(filter(str.isalpha, s))
    results = set()
    for p in permutations(filtered_chars):
        candidate = ''.join(p)
        if len(candidate) >= 4 and candidate == candidate[::-1]:
            results.add(candidate)
    return results