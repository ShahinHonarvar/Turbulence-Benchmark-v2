def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string) + 1):
            if len(set(input_string[i:j])) == 88 and input_string[i:j] not in substrings:
                substrings.append(input_string[i:j])
    return substrings