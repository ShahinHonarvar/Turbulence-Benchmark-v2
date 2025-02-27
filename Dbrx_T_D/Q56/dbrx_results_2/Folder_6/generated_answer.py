def all_substring_of_size_n(s):
    result = set()
    n = 23
    for i in range(len(s) - n + 1):
        substring = ''.join(sorted(s[i:i + n]))
        if len(substring) == n:
            result.add(substring)
    return list(result)