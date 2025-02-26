def all_substring_of_size_n(string):
    if len(string) < 67:
        return []
    result = []
    for i in range(len(string) - 66):
        substring = string[i:i + 67]
        if len(set(substring)) == 67:
            result.append(substring)
    return list(set(result))