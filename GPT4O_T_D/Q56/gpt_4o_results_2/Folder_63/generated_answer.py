def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 18):
        substring = s[i:i + 19]
        if len(set(substring)) == 19:
            if substring not in result:
                result.append(substring)
    return result