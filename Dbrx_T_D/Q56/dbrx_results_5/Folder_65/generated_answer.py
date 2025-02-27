def all_substring_of_size_n(s):
    if len(s) < 81:
        return []
    result = set()
    for i in range(len(s) - 80):
        substring = s[i:i + 81]
        if len(substring) == 81 and len(set(substring)) == 81:
            result.add(substring)
    return list(result)