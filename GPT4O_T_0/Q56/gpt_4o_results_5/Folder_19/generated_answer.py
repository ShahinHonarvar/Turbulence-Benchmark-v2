def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 17):
        substring = s[i:i + 18]
        if len(set(substring)) == 18:
            result.append(substring)
    return result