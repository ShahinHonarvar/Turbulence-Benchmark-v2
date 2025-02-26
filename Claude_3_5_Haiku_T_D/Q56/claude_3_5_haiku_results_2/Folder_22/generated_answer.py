def all_substring_of_size_n(s):
    if len(s) < 22:
        return []
    result = set()
    for i in range(len(s) - 21):
        substring = s[i:i + 22]
        if len(set(substring)) == 22:
            result.add(substring)
    return list(result)