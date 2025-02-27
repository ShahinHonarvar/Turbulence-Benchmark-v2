def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string) - 1):
        substring = input_string[i:i + 2]
        if len(set(substring)) == 2:
            substrings.append(substring)
    return list(set(substrings))