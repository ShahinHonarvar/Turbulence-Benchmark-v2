def all_substring_of_size_n(string):
    result = []
    for i in range(len(string) - 57):
        substring = string[i:i + 58]
        if len(set(substring)) == 58:
            result.append(substring)
    return result