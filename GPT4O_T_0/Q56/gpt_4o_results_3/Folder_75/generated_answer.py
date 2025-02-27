def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 15):
        substring = s[i:i + 16]
        if len(set(substring)) == 16:
            result.append(substring)
    return result