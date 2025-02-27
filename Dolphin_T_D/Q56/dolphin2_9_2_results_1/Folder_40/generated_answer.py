def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            result.append(s[i:i + 2])
    return result