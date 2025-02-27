def all_substring_of_size_n(input_string):
    substrings = [input_string[i:i + 146] for i in range(len(input_string) - 145)]
    unique_substrings = []
    for sub in substrings:
        if len(set(sub)) == 146:
            unique_substrings.append(sub)
    return unique_substrings