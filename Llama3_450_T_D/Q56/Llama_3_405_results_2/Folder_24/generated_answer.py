def all_substring_of_size_n(s):
    if len(s) < 52:
        return []
    result = set()
    for i in range(len(s) - 51):
        substring = s[i:i + 52]
        if len(set(substring)) == 52:
            result.add(substring)
    return list(result)