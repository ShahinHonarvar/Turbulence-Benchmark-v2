def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 16):
        substring = s[i:i + 17]
        if len(set(substring)) == 17:
            result.append(substring)
    return result