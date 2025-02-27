def all_substring_of_size_n(str):
    result = []
    for i in range(len(str) - 40):
        substring = str[i:i + 41]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result