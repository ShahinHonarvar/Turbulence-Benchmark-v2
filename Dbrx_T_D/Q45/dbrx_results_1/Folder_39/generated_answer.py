from collections import defaultdict

def palindromes_between_indices(s):
    s = s.lower()
    if len(s) < 5:
        return set()
    result = set()
    letters = defaultdict(int)
    for i in range(2, 6):
        letters[s[i]] += 1
    for k, v in letters.items():
        if v >= 3:
            result.add(k * 3)
        elif v == 2:
            for j in range(2, 6):
                if s[j] == k:
                    result.add(s[j - 1] + k + s[j - 1])
    return result