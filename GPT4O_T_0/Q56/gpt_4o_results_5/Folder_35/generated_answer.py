def all_substring_of_size_n(s):
    result = []
    n = len(s)
    for i in range(n - 26):
        substring = s[i:i + 27]
        if len(set(substring)) == 27:
            result.append(substring)
    return result