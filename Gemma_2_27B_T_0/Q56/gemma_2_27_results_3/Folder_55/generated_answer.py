def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 39):
        substring = s[i:i + 40]
        if len(set(substring)) == 40:
            result.append(substring)
    return result