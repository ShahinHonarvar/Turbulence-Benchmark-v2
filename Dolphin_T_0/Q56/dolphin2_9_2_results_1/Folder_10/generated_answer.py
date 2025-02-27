def all_substring_of_size_n(string):
    result = []
    for i in range(len(string) - 54):
        substring = string[i:i + 55]
        if len(set(substring)) == 55:
            result.append(substring)
    return result