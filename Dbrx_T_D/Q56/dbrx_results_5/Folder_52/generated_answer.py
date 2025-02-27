def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 14):
        substring = ''.join(sorted(s[i:i + 15]))
        if len(substring) == 15:
            result.add(substring)
    return list(result)