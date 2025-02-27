def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 44):
        substring = s[i:i + 45]
        if len(set(substring)) == 45:
            result.append(substring)
    return result