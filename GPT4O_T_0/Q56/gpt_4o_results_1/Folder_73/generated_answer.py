def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 19):
        substring = s[i:i + 20]
        if len(set(substring)) == 20:
            result.append(substring)
    return result