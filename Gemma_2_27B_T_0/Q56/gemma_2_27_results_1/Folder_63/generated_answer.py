def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 18):
        substring = s[i:i + 19]
        if len(set(substring)) == 19:
            result.append(substring)
    return result