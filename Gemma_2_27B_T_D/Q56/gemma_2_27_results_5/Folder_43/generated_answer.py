def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 85):
        substring = s[i:i + 86]
        if len(set(substring)) == 86:
            result.append(substring)
    return result