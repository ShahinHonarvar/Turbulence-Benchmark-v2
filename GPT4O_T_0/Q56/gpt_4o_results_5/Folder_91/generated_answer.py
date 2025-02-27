def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 5):
        substring = s[i:i + 6]
        if len(set(substring)) == 6:
            result.append(substring)
    return list(set(result))