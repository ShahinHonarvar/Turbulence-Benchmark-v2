def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 49):
        substring = s[i:i + 50]
        if len(set(substring)) == 50:
            if substring not in result:
                result.append(substring)
    return result