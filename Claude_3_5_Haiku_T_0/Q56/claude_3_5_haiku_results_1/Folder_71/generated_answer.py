def all_substring_of_size_n(s):
    if len(s) < 17:
        return []
    result = []
    for i in range(len(s) - 16):
        substring = s[i:i + 17]
        if len(set(substring)) == 17 and substring not in result:
            result.append(substring)
    return result