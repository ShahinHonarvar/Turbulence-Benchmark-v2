def all_substring_of_size_n(s):
    if len(s) < 16:
        return []
    result = set()
    for i in range(len(s) - 15):
        substring = s[i:i + 16]
        if len(set(substring)) == 16:
            result.add(substring)
    return list(result)