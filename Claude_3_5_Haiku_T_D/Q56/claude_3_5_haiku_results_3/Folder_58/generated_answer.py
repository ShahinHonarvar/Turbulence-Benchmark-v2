def all_substring_of_size_n(s):
    if len(s) < 127:
        return []
    result = set()
    for i in range(len(s) - 126):
        substring = s[i:i + 127]
        if len(set(substring)) == 127:
            result.add(substring)
    return list(result)