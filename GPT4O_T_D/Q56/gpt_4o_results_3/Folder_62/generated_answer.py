def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 31):
        substring = s[i:i + 32]
        if len(set(substring)) == 32:
            result.append(substring)
    return result