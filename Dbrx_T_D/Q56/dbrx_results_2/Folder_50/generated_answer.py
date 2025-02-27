from collections import defaultdict

def all_substring_of_size_n(s):
    n = 11
    if len(s) < n:
        return []
    substring_set = set()
    substring_dict = defaultdict(list)
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        sorted_substring = ''.join(sorted(substring))
        if len(substring) == len(set(substring)):
            substring_set.add(substring)
        substring_dict[sorted_substring].append(substring)
    return list(substring_set.union(substring_dict[next(iter(substring_dict))]))