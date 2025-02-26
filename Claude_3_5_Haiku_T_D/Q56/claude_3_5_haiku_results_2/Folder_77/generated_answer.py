def all_substring_of_size_n(s):
    if len(s) < 144:
        return []
    result = set()
    for i in range(len(s) - 143):
        substring = s[i:i + 144]
        if len(set(substring)) == 144:
            result.add(substring)
    return list(result)