def all_substring_of_size_n(string):
    result = []
    for i in range(len(string) - 39):
        sub_string = string[i:i + 40]
        if len(set(sub_string)) == 40:
            result.append(sub_string)
    return result