def all_substring_of_size_n(s):
    n = len(s)
    result = []
    for i in range(n - 104):
        substring = s[i:i + 105]
        if len(set(substring)) == 105:
            result.append(substring)
    return result