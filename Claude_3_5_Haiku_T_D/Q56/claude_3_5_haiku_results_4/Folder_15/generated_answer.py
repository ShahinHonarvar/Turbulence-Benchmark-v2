def all_substring_of_size_n(s):
    if len(s) < 3:
        return []
    result = set()
    for i in range(len(s) - 2):
        substring = s[i:i + 3]
        if len(set(substring)) == 3:
            result.add(substring)
    return list(result)