def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 55):
        substring = s[i:i + 56]
        if len(set(substring)) == 56:
            result.append(substring)
    return result