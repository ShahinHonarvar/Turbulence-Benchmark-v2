def all_substring_of_size_n(s):
    substring_size = 84
    result = set()
    for i in range(len(s) - substring_size + 1):
        substring = s[i:i + substring_size]
        if len(substring) == substring_size and len(set(substring)) == substring_size:
            result.add(substring)
    return list(result)