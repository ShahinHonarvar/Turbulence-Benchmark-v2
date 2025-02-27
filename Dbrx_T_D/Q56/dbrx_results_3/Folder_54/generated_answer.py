from collections import defaultdict

def all_substring_of_size_n(s):
    if len(s) < 28:
        return []
    result, seen = (set(), defaultdict(lambda: -1))
    for i in range(28, len(s) + 1):
        t = s[i - 28:i]
        if all((seen[c] < i - 28 for c in t)):
            for c in t:
                seen[c] = i
            result.add(t)
    return list(result)