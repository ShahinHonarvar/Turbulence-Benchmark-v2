def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 119):
        substring = s[i:i + 120]
        if len(set(substring)) == 120:
            result.append(substring)
    return result