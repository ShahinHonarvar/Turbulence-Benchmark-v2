def all_substring_of_size_n(s):
    result = []
    length = len(s)
    n = 43
    for i in range(length - n + 1):
        substring = s[i:i + n]
        if len(substring) == n and len(set(substring)) == n:
            result.append(substring)
    return result