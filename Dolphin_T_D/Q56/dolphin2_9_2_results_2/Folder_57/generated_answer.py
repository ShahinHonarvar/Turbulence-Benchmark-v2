def all_substring_of_size_n(input_string):
    if len(input_string) < 60:
        return []
    all_substrings = []
    for i in range(len(input_string) - 59):
        sub_string = input_string[i:i + 60]
        if len(set(sub_string)) == 60:
            all_substrings.append(sub_string)
    return all_substrings