def all_substring_of_size_n(s):
    if len(s) < 8:
        return []
    result = []
    for i in range(len(s) - 7):
        substring = s[i:i + 8]
        if len(set(substring)) == 8 and substring not in result:
            result.append(substring)
    return result