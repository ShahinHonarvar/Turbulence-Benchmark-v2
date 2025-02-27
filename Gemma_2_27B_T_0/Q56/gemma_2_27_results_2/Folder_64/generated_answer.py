def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 7):
        substring = s[i:i + 8]
        if len(set(substring)) == 8:
            result.append(substring)
    return result