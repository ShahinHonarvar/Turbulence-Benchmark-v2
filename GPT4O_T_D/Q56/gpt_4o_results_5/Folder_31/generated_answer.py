def all_substring_of_size_n(s):
    n = len(s)
    result = []
    for i in range(n - 46 + 1):
        substring = s[i:i + 46]
        if len(set(substring)) == 46:
            result.append(substring)
    return result