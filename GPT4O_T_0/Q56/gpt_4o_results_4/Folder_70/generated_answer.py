def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 11):
        substring = s[i:i + 12]
        if len(set(substring)) == 12:
            result.append(substring)
    return result