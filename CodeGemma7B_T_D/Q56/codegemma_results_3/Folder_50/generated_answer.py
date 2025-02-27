def all_substring_of_size_n(str):
    result = []
    for i in range(len(str) - 10):
        substring = str[i:i + 11]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result