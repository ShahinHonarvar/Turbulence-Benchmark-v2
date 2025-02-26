def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 57):
        substring = s[i:i + 58]
        if len(set(substring)) == 58:
            result.add(substring)
    return list(result)