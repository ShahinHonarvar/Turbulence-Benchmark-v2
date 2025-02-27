def all_substring_of_size_n(string):
    result = []
    length = len(string)
    for i in range(length - 63):
        substring = string[i:i + 64]
        if len(set(substring)) == 64:
            result.append(substring)
    return result