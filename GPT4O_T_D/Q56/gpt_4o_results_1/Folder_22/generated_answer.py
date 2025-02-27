def all_substring_of_size_n(s):
    result = []
    length = len(s)
    for i in range(length - 21):
        substr = s[i:i + 22]
        if len(substr) == 22 and len(set(substr)) == 22:
            result.append(substr)
    return result