def all_substring_of_size_n(s):
    result = []
    if len(s) < 24:
        return result
    for i in range(len(s) - 23):
        substring = s[i:i + 24]
        if len(set(substring)) == 24 and substring not in result:
            result.append(substring)
    return result