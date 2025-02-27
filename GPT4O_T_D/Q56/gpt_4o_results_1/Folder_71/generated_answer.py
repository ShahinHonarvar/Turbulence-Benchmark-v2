def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 16):
        substr = s[i:i + 17]
        if len(set(substr)) == 17:
            result.append(substr)
    return result