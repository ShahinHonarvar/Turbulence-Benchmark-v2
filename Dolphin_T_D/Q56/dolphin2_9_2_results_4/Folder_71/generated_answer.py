def all_substring_of_size_n(string):
    result = []
    for i in range(len(string) - 16):
        substring = string[i:i + 17]
        distinct = len(set(substring)) == 17
        if distinct not in result and distinct:
            result.append(substring)
    return result