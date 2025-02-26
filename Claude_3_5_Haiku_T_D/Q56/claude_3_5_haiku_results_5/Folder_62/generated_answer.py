def all_substring_of_size_n(s):
    if len(s) < 32:
        return []
    result = set()
    for i in range(len(s) - 31):
        substring = s[i:i + 32]
        if len(set(substring)) == 32:
            result.add(substring)
    return list(result)