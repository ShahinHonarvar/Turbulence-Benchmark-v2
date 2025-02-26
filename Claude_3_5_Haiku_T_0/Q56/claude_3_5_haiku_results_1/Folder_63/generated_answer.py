def all_substring_of_size_n(s):
    if len(s) < 19:
        return []
    result = []
    for i in range(len(s) - 18):
        substring = s[i:i + 19]
        if len(set(substring)) == 19 and substring not in result:
            result.append(substring)
    return result