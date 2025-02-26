def all_substring_of_size_n(s):
    result = set()
    if len(s) < 11:
        return list(result)
    for i in range(len(s) - 10):
        substring = s[i:i + 11]
        if len(set(substring)) == 11:
            result.add(substring)
    return list(result)