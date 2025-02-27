def all_substring_of_size_n(s):
    n = 65
    result = []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == len(set(substring)) == n:
            result.append(substring)
    return result