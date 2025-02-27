def all_substring_of_size_n(string):
    result = []
    for i in range(len(string) - 19):
        if len(set(string[i:i + 20])) == 20:
            result.append(string[i:i + 20])
    return result