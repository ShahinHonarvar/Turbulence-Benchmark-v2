def all_substring_of_size_n(string):
    length = len(string)
    result = []
    for i in range(length - 55):
        substring = string[i:i + 56]
        if len(set(substring)) == 56:
            result.append(substring)
    return result