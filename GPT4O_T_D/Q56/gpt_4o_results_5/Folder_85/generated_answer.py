def all_substring_of_size_n(s):
    result = []
    length = len(s)
    for i in range(length - 13):
        substring = s[i:i + 14]
        if len(set(substring)) == 14:
            result.append(substring)
    return list(set(result))