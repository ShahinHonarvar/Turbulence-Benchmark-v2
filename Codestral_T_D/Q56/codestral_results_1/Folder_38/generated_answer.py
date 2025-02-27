def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string) - 34):
        substring = input_string[i:i + 35]
        if len(set(substring)) == 35:
            substrings.append(substring)
    return substrings