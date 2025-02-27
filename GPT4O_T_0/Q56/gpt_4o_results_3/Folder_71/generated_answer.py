def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 16):
        substring = s[i:i + 17]
        if len(set(substring)) == 17:
            result.append(substring)
    return result