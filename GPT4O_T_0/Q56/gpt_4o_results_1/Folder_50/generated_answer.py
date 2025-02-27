def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 10):
        substring = s[i:i + 11]
        if len(set(substring)) == 11:
            result.append(substring)
    return result