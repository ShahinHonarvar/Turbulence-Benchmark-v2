def all_substring_of_size_n(string):
    if len(string) < 11:
        return []
    result = []
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            substring = string[i:j + 1]
            if len(substring) == 11 and len(set(substring)) == len(substring):
                result.append(substring)
    return result