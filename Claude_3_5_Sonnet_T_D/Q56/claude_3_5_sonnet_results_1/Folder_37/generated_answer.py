def all_substring_of_size_n(s):
    result = []
    n = 65
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            if substring not in result:
                result.append(substring)
    return result