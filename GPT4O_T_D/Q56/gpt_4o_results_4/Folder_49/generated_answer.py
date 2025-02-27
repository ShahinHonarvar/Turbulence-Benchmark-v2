def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 72):
        substring = s[i:i + 73]
        if len(set(substring)) == 73:
            result.append(substring)
    return result