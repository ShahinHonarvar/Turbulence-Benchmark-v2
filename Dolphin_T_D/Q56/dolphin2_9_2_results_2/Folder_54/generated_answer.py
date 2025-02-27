def all_substring_of_size_n(s):
    length = len(s)
    n = 28
    result = []
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            result.append(substring)
    return result