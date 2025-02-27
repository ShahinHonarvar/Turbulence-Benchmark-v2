import itertools

def palindromes_between_indices(s):
    s = s.lower()
    if len(s) < 9:
        return set()
    sub = ''.join([ch for ch in s[5:9] if ch.isalpha()])
    results = set()
    if len(sub) < 3:
        return results
    for r in range(3, len(sub) + 1):
        for combo in itertools.permutations(sub, r):
            word = ''.join(combo)
            if word == word[::-1]:
                results.add(word)
    return results