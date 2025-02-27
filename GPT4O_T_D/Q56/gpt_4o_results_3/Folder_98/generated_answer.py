def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 9):
        substr = s[i:i + 10]
        if len(set(substr)) == 10:
            result.append(substr)
    return result