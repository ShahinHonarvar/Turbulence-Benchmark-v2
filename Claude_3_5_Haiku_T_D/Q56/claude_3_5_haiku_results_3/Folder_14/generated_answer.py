def all_substring_of_size_n(s):
    if len(s) < 85:
        return []
    result = set()
    for i in range(len(s) - 84):
        substring = s[i:i + 85]
        if len(set(substring)) == 85:
            result.add(substring)
    return list(result)