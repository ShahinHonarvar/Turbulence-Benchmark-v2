def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 53):
        substring = s[i:i + 54]
        if len(set(substring)) == 54:
            result.append(substring)
    return result