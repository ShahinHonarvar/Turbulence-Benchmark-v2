def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 40):
        substring = s[i:i + 41]
        if len(set(substring)) == 41:
            result.append(substring)
    return result