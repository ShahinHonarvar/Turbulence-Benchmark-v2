def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 91):
        substring = s[i:i + 92]
        if len(set(substring)) == 92:
            result.append(substring)
    return result