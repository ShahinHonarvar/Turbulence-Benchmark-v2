def all_substring_of_size_n(s):
    if len(s) < 42:
        return []
    result = []
    for i in range(len(s) - 41):
        substring = s[i:i + 42]
        if len(set(substring)) == 42:
            result.append(substring)
    return list(dict.fromkeys(result))