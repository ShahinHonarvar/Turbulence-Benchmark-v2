def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 20):
        substring = s[i:i + 21]
        if len(set(substring)) == 21:
            result.append(substring)
    return result