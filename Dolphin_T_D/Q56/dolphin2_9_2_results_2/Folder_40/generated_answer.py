def all_substring_of_size_n(s):
    result = []
    for i in range(len(s)):
        if i + 1 < len(s) and s[i] != s[i + 1]:
            result.append(s[i:i + 2])
    return result