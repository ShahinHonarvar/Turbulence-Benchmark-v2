def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 49 + 1):
        substring = s[i:i + 49]
        if len(set(substring)) == 49:
            result.add(substring)
    return list(result)