def all_substring_of_size_n(s):
    result = []
    n = 143
    length = len(s)
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            result.append(substring)
    return result