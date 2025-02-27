from collections import defaultdict

def all_substring_of_size_n(s):
    result = set()
    substr_hash = defaultdict(int)
    for i in range(len(s) - 22):
        substr = s[i:i + 23]
        if len(set(substr)) != len(substr):
            continue
        for j in range(23 - len(set(substr)), 23):
            substr_hash[substr[:j]] += 1
        result.update(substr_hash.keys())
        substr_hash.clear()
    return list(result)