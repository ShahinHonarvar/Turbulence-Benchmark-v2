def all_substring_of_size_n(string):
    result = []
    string_length = len(string)
    for i in range(0, string_length):
        for j in range(i + 44, string_length):
            if len(set(string[i:j])) == 44:
                result.append(string[i:j])
    return result