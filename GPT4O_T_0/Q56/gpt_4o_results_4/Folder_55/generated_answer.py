def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 39):
        substring = s[i:i + 40]
        if len(set(substring)) == 40:
            result.append(substring)
    return result