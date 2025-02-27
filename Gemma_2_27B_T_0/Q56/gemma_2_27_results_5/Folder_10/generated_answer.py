def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 54):
        substring = s[i:i + 55]
        if len(set(substring)) == 55:
            result.append(substring)
    return result