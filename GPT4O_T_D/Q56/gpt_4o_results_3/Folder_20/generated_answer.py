def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 49):
        substring = s[i:i + 50]
        if len(substring) == 50 and len(set(substring)) == 50:
            result.append(substring)
    return result