def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 35):
        substr = s[i:i + 36]
        if len(substr) == 36 and len(set(substr)) == 36:
            result.append(substr)
    return result