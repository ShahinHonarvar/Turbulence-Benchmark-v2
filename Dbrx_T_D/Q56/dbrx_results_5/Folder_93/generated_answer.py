def all_substring_of_size_n(s):
    result = []
    if len(s) < 54:
        return result
    for i in range(len(s) - 54 + 1):
        substring = s[i:i + 54]
        if len(set(substring)) == 54:
            result.append(substring)
    return list(set(result))