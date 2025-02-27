def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string) - 16):
        substring = input_string[i:i + 17]
        if len(set(substring)) == 17:
            substrings.append(substring)
    return substrings