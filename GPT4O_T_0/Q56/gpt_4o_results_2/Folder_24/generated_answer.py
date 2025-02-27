def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 51):
        substring = s[i:i + 52]
        if len(set(substring)) == 52:
            result.append(substring)
    return result