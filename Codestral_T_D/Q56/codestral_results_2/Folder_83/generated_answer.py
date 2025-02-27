def all_substring_of_size_n(input_string):
    substrings = []
    str_len = len(input_string)
    for i in range(str_len - 47):
        sub = input_string[i:i + 48]
        if len(set(sub)) == 48:
            substrings.append(sub)
    return substrings