def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 23 + 1):
        substring = s[i:i + 23]
        if len(set(substring)) == 23:
            result.add(substring)
    return list(result)