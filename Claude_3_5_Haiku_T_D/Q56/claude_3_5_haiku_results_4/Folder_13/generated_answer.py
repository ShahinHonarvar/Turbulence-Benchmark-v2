def all_substring_of_size_n(s):
    if len(s) < 53:
        return []
    result = set()
    for i in range(len(s) - 52):
        substring = s[i:i + 53]
        if len(set(substring)) == 53:
            result.add(substring)
    return list(result)