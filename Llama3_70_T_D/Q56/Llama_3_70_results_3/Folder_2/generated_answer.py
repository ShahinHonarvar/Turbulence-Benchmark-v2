def all_substring_of_size_n(s):
    length = len(s)
    result = set()
    for i in range(length - 55):
        substring = s[i:i + 56]
        if len(set(substring)) == 56:
            result.add(substring)
    return list(result)