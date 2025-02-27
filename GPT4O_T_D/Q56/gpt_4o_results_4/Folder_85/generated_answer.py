def all_substring_of_size_n(s):
    if len(s) < 14:
        return []
    result = []
    for i in range(len(s) - 13):
        sub_str = s[i:i + 14]
        if len(set(sub_str)) == 14:
            result.append(sub_str)
    return list(set(result))