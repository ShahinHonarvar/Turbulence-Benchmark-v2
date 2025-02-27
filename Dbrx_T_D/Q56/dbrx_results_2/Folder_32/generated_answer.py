def all_substring_of_size_n(string):
    result = []
    char_set = set()
    n = 71
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(char_set & set(substring)) == 0:
            result.append(substring)
            char_set.update(substring)
    return result