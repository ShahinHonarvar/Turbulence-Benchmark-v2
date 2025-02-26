def all_substring_of_size_n(s):
    if len(s) < 79:
        return []
    result = set()
    for i in range(len(s) - 78):
        substring = s[i:i + 79]
        if len(set(substring)) == 79:
            result.add(substring)
    return list(result)