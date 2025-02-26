def all_substring_of_size_n(s):
    if len(s) < 20:
        return []
    result = []
    for i in range(len(s) - 19):
        substring = s[i:i + 20]
        if len(set(substring)) == 20 and substring not in result:
            result.append(substring)
    return result