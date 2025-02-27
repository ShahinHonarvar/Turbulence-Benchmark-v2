def all_substring_of_size_n(string):
    if len(string) < 28:
        return []
    result = []
    for i in range(len(string) - 27):
        substring = string[i:i + 28]
        if len(set(substring)) == len(substring):
            result.append(substring)
    return result