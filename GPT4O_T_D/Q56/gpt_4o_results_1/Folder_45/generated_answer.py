def all_substring_of_size_n(s):
    result = []
    length = len(s)
    for i in range(length - 28):
        substring = s[i:i + 29]
        if len(set(substring)) == 29:
            result.append(substring)
    return result