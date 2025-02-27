def all_substring_of_size_n(string):
    length = 42
    result = []
    if len(string) < length:
        return result
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        if len(set(substring)) == length:
            result.append(substring)
    return result