def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string) - 63):
        current_substring = input_string[i:i + 64]
        if len(set(current_substring)) == 64:
            substrings.append(current_substring)
    return substrings