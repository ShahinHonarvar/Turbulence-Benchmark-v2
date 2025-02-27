def all_substring_of_size_n(string):
    result = []
    for i in range(len(string) - 7):
        if len(set(string[i:i + 84])) == 84:
            result.append(string[i:i + 84])
    result = list(set(result))
    return result