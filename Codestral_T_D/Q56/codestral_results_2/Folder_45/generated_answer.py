def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string) - 28):
        sub = input_string[i:i + 29]
        if len(set(sub)) == 29:
            substrings.append(sub)
    return substrings