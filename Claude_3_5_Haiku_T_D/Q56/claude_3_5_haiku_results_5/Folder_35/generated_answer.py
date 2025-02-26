def all_substring_of_size_n(s):
    if len(s) < 27:
        return []
    result = set()
    for i in range(len(s) - 26):
        substring = s[i:i + 27]
        if len(set(substring)) == 27:
            result.add(substring)
    return list(result)