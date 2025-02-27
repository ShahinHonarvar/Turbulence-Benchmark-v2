def all_substring_of_size_n(string):
    n = 77
    result = []
    for i in range(len(string) - n + 1):
        substr = string[i:i + n]
        if len(set(substr)) == n:
            result.append(substr)
    return result