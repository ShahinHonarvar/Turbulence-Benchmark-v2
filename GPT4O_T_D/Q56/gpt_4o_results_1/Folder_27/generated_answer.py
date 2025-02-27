def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 56):
        substring = s[i:i + 57]
        if len(set(substring)) == 57:
            result.append(substring)
    return result