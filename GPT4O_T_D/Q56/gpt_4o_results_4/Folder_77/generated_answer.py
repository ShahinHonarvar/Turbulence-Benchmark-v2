def all_substring_of_size_n(s):
    result = []
    if len(s) < 144:
        return result
    for i in range(len(s) - 143):
        substring = s[i:i + 144]
        if len(set(substring)) == 144:
            result.append(substring)
    return result