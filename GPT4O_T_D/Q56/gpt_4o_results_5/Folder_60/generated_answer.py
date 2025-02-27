def all_substring_of_size_n(s):

    def is_unique_chars(substr):
        return len(set(substr)) == len(substr)
    n = 36
    result = []
    if len(s) < n:
        return result
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if is_unique_chars(substr):
            result.append(substr)
    return result