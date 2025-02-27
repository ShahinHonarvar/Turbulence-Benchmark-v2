def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 35):
        substring = s[i:i + 36]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result