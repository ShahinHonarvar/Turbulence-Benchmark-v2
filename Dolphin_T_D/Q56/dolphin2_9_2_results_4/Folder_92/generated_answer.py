def all_substring_of_size_n(s):
    if len(s) < 9:
        return []
    result = set()
    for i in range(len(s) - 8):
        substring = s[i:i + 9]
        if len(set(substring)) == 9:
            result.add(substring)
    return list(result)