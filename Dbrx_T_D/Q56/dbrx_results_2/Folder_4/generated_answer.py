def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 40):
        substring = s[i:i + 41]
        if len(substring) == 41 and len(set(substring)) == 41:
            result.add(substring)
    return list(result)