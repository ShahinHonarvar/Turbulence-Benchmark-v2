def all_substring_of_size_n(s):
    if len(s) < 42:
        return []
    result = {}
    for i in range(len(s) - 41):
        sub = s[i:i + 42]
        if len(set(sub)) == len(sub):
            result[sub] = 1
    return list(result.keys())