def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 59):
        substring = s[i:i + 60]
        if len(set(substring)) == 60:
            result.append(substring)
    return result