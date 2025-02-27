from collections import defaultdict

def all_substring_of_size_n(s):
    mp = defaultdict(bool)
    res = set()
    for i in range(28, len(s) + 1):
        substring = s[i - 28:i]
        if not mp[substring]:
            res.add(substring)
            mp[substring] = True
    return sorted(res)