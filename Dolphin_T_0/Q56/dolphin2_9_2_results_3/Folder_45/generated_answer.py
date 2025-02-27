def all_substring_of_size_n(string):
    if len(string) < 29:
        return []
    output = []
    for i in range(len(string) - 28):
        if len(set(string[i:i + 29])) == 29:
            output.append(string[i:i + 29])
    return output