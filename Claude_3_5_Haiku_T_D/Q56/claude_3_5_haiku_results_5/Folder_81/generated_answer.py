def all_substring_of_size_n(s):
    if len(s) < 98:
        return []
    result = set()
    for i in range(len(s) - 97):
        substring = s[i:i + 98]
        if len(set(substring)) == 98:
            result.add(substring)
    return list(result)