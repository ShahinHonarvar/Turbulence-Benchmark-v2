def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string) - 49):
        substring = input_string[i:i + 50]
        if len(set(substring)) == 50:
            substrings.append(substring)
    return substrings