def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 14):
        substring = s[i:i + 15]
        if len(set(substring)) == 15:
            result.append(substring)
    return result