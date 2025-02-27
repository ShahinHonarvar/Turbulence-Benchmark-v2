def all_substring_of_size_n(s):
    result = []
    n = len(s)
    substring_length = 33
    for i in range(n - substring_length + 1):
        substring = s[i:i + substring_length]
        if len(set(substring)) == substring_length:
            result.append(substring)
    return result