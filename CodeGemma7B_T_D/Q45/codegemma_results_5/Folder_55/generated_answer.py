from itertools import permutations

def palindromes_between_indices(s):
    seen = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            word = ''.join((p for p in permutations(s[i:j + 1]) if p[0] != '0'))
            if word.lower() not in seen:
                seen.add(word.lower())
    return seen