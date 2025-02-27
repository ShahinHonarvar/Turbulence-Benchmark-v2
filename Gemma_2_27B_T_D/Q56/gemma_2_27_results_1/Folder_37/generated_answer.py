def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 64):
        substring = s[i:i + 65]
        if len(set(substring)) == 65:
            result.append(substring)
    return result