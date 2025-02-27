def all_substring_of_size_n(s):
    result = []
    length = len(s)
    for i in range(length - 70):
        substr = s[i:i + 71]
        if len(set(substr)) == 71:
            result.append(substr)
    return result