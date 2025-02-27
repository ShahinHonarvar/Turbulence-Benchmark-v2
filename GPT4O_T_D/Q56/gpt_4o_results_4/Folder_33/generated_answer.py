def all_substring_of_size_n(s):
    result = []
    str_len = len(s)
    for i in range(str_len - 104):
        substr = s[i:i + 105]
        if len(set(substr)) == 105:
            result.append(substr)
    return result