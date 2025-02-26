def all_substring_of_size_n(s):
    if len(s) < 14:
        return []
    result = []
    for i in range(len(s) - 13):
        substring = s[i:i + 14]
        if len(set(substring)) == 14 and substring not in result:
            result.append(substring)
    return result