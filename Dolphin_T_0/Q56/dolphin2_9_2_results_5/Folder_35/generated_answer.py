def all_substring_of_size_n(s):
    if len(set(s)) != len(s):
        return []
    result = set()
    for i in range(len(s) - 26):
        result.add(s[i:i + 27])
    return list(result)