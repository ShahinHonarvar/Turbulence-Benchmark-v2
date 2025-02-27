def all_substring_of_size_n(input_string):
    substrings = []
    length = len(input_string)
    for i in range(length - 54):
        substring = input_string[i:i + 55]
        if len(set(substring)) == 55:
            substrings.append(substring)
    return substrings