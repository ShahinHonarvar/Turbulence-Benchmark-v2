def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 40):
        substr = s[i:i + 40]
        if len(set(substr)) == 40:
            result.append(substr)
    return result