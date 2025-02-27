def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 55 + 1):
        substring = s[i:i + 55]
        if len(set(substring)) == 55:
            result.add(substring)
    return list(result)