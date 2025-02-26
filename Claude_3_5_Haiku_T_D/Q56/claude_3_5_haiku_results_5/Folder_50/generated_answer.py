def all_substring_of_size_n(s):
    if len(s) < 11:
        return []
    result = set()
    for i in range(len(s) - 10):
        substring = s[i:i + 11]
        if len(set(substring)) == 11:
            result.add(substring)
    return list(result)