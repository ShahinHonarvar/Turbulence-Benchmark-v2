def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            result.add(s[i:i + 2])
    return list(result)