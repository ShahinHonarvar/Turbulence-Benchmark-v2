def all_substring_of_size_n(input_string):
    substrings = set()
    for i in range(len(input_string) - 7):
        substring = input_string[i:i + 8]
        if len(set(substring)) == 8:
            substrings.add(substring)
    return list(substrings)