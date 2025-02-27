def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 29):
        substring = s[i:i + 30]
        if len(set(substring)) == 30:
            result.append(substring)
    return result