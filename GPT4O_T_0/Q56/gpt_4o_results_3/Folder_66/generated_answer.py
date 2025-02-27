def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 25):
        substring = s[i:i + 26]
        if len(set(substring)) == 26:
            result.append(substring)
    return result