def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 76):
        substring = s[i:i + 77]
        if len(set(substring)) == 77:
            result.add(substring)
    return list(result)