from collections import defaultdict

def all_substring_of_size_n(s):
    n = 85
    if len(s) < n:
        return []
    substrs = []
    substr_count = defaultdict(int)
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(substr) != n:
            continue
        is_unique = True
        for char in substr:
            if substr_count[char] > 0:
                is_unique = False
                break
            substr_count[char] += 1
        if is_unique:
            substrs.append(substr)
        for char in substr:
            substr_count[char] -= 1
    return list(set(substrs))