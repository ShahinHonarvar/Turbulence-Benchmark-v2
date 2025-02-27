from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = []
    for i in range(6, 10):
        if 97 <= ord(s[i]) <= 122:
            letters.append(s[i])
    result = set()
    for i in range(5, len(letters) + 1):
        for p in permutations(letters, i):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result