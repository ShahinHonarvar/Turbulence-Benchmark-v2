def all_substring_of_size_n(input_string):
    result = []
    for i in range(len(input_string) - 13):
        sub = input_string[i:i + 14]
        if len(set(sub)) == 14:
            result.append(sub)
    return result