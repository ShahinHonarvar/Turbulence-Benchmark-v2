def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 2):
        substring = s[i:i + 3]
        if len(substring) == 3 and len(set(substring)) == 3:
            result.add(substring)
    return list(result)