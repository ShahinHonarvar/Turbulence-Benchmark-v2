def all_substring_of_size_n(input_string):
    substrings = set()
    for i in range(len(input_string) - 62):
        sub_string = input_string[i:i + 63]
        if len(set(sub_string)) == 63:
            substrings.add(sub_string)
    return list(substrings)