def all_substring_of_size_n(string):
    result = []
    for i in range(len(string) - 7):
        if len(set(string[i:i + 8])) == 8 and string[i:i + 8] not in result:
            result.append(string[i:i + 8])
    return result