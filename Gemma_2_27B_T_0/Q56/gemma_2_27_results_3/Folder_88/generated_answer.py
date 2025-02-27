def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 67):
        substring = s[i:i + 68]
        if len(set(substring)) == 68:
            result.append(substring)
    return result