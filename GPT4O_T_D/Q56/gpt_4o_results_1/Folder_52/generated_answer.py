def all_substring_of_size_n(s):
    result = []
    length = len(s)
    for i in range(length - 14):
        substring = s[i:i + 15]
        if len(substring) == 15 and len(set(substring)) == 15:
            result.append(substring)
    return result