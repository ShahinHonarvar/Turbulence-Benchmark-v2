def all_substring_of_size_n(str):
    result = []
    for i in range(len(str) - 53):
        substring = str[i:i + 54]
        if len(set(substring)) == 54:
            result.append(substring)
    return result