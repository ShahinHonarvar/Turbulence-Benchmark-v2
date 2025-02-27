def all_substring_of_size_n(s):
    result = set()
    if len(s) < 19:
        return []
    for i in range(len(s)):
        if len(set(s[i:i + 19])) == 19:
            result.add(s[i:i + 19])
    return list(result)