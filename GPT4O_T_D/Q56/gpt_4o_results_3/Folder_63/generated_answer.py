def all_substring_of_size_n(s):
    result = []
    length = len(s)
    for i in range(length - 18):
        substring = s[i:i + 19]
        if len(set(substring)) == 19:
            result.append(substring)
    return result