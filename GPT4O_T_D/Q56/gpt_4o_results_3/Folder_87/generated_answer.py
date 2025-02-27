def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 57):
        substring = s[i:i + 58]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result