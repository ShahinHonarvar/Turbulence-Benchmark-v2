def all_substring_of_size_n(s):
    if len(s) < 88:
        return []
    result = set()
    for i in range(len(s) - 87):
        substring = s[i:i + 88]
        if len(set(substring)) == 88:
            result.add(substring)
    return list(result)