def all_substring_of_size_n(s):
    if len(s) < 92:
        return []
    result = set()
    for i in range(len(s) - 91):
        substring = s[i:i + 92]
        if len(set(substring)) == 92:
            result.add(substring)
    return list(result)