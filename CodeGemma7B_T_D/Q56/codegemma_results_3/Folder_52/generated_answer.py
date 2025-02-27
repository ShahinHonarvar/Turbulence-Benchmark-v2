def all_substring_of_size_n(string):
    result = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if len(substring) == 15 and len(set(substring)) == 15:
                result.append(substring)
    return result