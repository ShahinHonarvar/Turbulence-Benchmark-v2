def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 62):
        result.add(s[i:i + 63])
    return list(result)