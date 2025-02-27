from collections import defaultdict

def all_substring_of_size_n(s):
    result = set()
    n = 97
    if len(s) < n:
        return []
    count = defaultdict(int)
    for i in range(n):
        count[s[i]] += 1
    for i in range(len(s) - n + 1):
        if len(count) == 97:
            result.add(s[i:i + n])
        count[s[i]] -= 1
        if count[s[i]] == 0:
            del count[s[i]]
        count[s[i + n]] += 1
    return list(result)