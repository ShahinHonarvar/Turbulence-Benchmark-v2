def all_substring_of_size_n(str):
    result = []
    for i in range(len(str) - 48 + 1):
        substring = str[i:i + 48]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result