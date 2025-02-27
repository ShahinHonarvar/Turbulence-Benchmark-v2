def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 37):
        substring = s[i:i + 38]
        if len(substring) == 38 and len(set(substring)) == 38:
            result.append(substring)
    return result