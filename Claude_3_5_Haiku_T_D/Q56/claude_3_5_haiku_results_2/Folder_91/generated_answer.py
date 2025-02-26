def all_substring_of_size_n(s):
    if len(s) < 6:
        return []
    result = set()
    for i in range(len(s) - 5):
        substring = s[i:i + 6]
        if len(set(substring)) == 6:
            result.add(substring)
    return list(result)