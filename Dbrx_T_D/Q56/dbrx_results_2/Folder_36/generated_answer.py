def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 146 + 1):
        substring = ''.join(sorted(s[i:i + 146]))
        if len(substring) == 146:
            result.add(substring)
    return list(result)