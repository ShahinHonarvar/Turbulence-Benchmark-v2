def all_substring_of_size_n(s):
    n = len(s)
    result = []
    for i in range(n - 56):
        if len(set(s[i:i + 57])) == 57:
            result.append(s[i:i + 57])
    return result