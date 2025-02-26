def all_substring_of_size_n(s):
    if len(s) < 31:
        return []
    result = []
    for i in range(len(s) - 30):
        substring = s[i:i + 31]
        if len(set(substring)) == 31 and substring not in result:
            result.append(substring)
    return result