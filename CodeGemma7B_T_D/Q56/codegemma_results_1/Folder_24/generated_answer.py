def all_substring_of_size_n(string):
    result = []
    for i in range(len(string) - 52 + 1):
        substring = string[i:i + 52]
        if len(set(substring)) == 52:
            result.append(substring)
    return result