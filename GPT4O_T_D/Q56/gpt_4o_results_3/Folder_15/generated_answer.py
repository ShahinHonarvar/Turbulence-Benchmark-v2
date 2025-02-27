def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 2):
        substr = s[i:i + 3]
        if len(set(substr)) == 3:
            result.append(substr)
    return list(set(result))