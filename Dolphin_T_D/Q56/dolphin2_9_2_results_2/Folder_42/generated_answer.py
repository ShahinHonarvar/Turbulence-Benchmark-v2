def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 44):
        substr = s[i:i + 45]
        if len(set(substr)) == 45:
            result.append(substr)
    return result