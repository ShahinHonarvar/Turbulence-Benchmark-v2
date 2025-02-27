def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 13):
        substring = s[i:i + 14]
        if len(set(substring)) == 14:
            result.append(substring)
    return result