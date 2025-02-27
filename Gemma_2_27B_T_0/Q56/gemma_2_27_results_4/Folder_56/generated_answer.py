def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 68):
        substring = s[i:i + 69]
        if len(set(substring)) == 69:
            result.append(substring)
    return result