def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 26):
        substring = s[i:i + 26]
        if len(set(substring)) == 26:
            result.append(substring)
    return result