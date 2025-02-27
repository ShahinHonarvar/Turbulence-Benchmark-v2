def all_substrings_of_size_n(input_string):
    substrings = {}
    for i in range(len(input_string) - 8):
        substring = input_string[i:i + 9]
        if len(set(substring)) == 9:
            substrings[substring] = True
    return list(substrings.keys())