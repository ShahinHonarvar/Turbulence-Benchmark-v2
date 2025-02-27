def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 27):
        substring = s[i:i + 28]
        if len(set(substring)) == 28:
            result.append(substring)
    return result