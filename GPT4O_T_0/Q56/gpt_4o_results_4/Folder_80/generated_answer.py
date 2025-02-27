def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 30):
        substring = s[i:i + 31]
        if len(set(substring)) == 31:
            result.append(substring)
    return result