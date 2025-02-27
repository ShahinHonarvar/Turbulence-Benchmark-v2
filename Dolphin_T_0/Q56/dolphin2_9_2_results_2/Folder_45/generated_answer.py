def all_substring_of_size_n(input_string):
    if len(input_string) < 29:
        return []
    substrings = set()
    for i in range(len(input_string) - 28):
        temp_string = input_string[i:i + 29]
        if len(set(temp_string)) == len(temp_string):
            substrings.add(temp_string)
    return list(substrings)