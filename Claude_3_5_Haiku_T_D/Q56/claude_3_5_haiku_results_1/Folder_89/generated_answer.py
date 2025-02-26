def all_substring_of_size_n(s):
    if len(s) < 38:
        return []
    result = []
    for i in range(len(s) - 37):
        substring = s[i:i + 38]
        if len(set(substring)) == 38 and substring not in result:
            result.append(substring)
    return result