def all_substring_of_size_n(s):
    if len(s) < 99 or len(set(s)) != len(s):
        return []
    result = []
    for i in range(len(s) - 98):
        substring = s[i:i + 99]
        result.append(substring)
    return list(set(result))