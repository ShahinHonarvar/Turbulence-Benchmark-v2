def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 127 + 1):
        substring = s[i:i + 127]
        if len(set(substring)) == 127:
            result.append(substring)
    return result