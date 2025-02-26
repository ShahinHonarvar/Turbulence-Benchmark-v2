def all_substring_of_size_n(s):
    if len(s) < 73:
        return []
    result = set()
    for i in range(len(s) - 72):
        substring = s[i:i + 73]
        if len(set(substring)) == 73:
            result.add(substring)
    return list(result)