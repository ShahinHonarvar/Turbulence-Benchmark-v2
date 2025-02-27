def all_substring_of_size_n(s):
    result = []
    length = len(s)
    for i in range(length - 17):
        substr = s[i:i + 18]
        if len(substr) == 18 and len(set(substr)) == 18:
            result.append(substr)
    return result