def all_substring_of_size_n(s):
    if len(s) < 50:
        return []
    result = []
    for i in range(len(s) - 49):
        substring = s[i:i + 50]
        if len(set(substring)) == 50:
            result.append(substring)
    return list(set(result))