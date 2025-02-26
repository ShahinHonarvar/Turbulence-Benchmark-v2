def all_substring_of_size_n(s):
    if len(s) < 18:
        return []
    result = []
    for i in range(len(s) - 17):
        substring = s[i:i + 18]
        if len(set(substring)) == 18 and substring not in result:
            result.append(substring)
    return result