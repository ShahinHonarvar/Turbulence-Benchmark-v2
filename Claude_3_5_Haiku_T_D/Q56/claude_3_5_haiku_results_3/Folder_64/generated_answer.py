def all_substring_of_size_n(string):
    if len(string) < 8:
        return []
    result = []
    for i in range(len(string) - 7):
        substring = string[i:i + 8]
        if len(set(substring)) == 8 and substring not in result:
            result.append(substring)
    return result