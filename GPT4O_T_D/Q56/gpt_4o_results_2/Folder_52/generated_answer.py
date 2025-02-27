def all_substring_of_size_n(s):
    result = []
    length = len(s)
    for i in range(length - 14):
        substring = s[i:i + 15]
        if len(set(substring)) == 15:
            result.append(substring)
    return list(set(result))