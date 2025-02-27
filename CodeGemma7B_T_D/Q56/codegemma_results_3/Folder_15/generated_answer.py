def all_substring_of_size_n(s):
    result = set()
    if len(s) < 3:
        return list(result)
    for i in range(len(s) - 2):
        for j in range(i + 1, len(s) - 1):
            for k in range(j + 1, len(s)):
                substring = s[i:k + 1]
                if len(substring) == len(set(substring)):
                    result.add(substring)
    return list(result)