def all_substring_of_size_n(s):
    if len(s) < 84:
        return []
    result = set()
    for i in range(len(s) - 83):
        substring = s[i:i + 84]
        if len(set(substring)) == 84:
            result.add(substring)
    return list(result)