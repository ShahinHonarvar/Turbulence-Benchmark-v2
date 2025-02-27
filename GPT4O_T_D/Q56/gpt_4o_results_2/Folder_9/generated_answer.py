def all_substring_of_size_n(s):
    result = []
    n = len(s)
    if n < 34:
        return result
    for i in range(n - 33):
        substring = s[i:i + 34]
        if len(substring) == len(set(substring)) == 34:
            result.append(substring)
    return result