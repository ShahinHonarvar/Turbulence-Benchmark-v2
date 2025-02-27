def all_substring_of_size_n(input_string):
    unique_substrings = set()
    for i in range(len(input_string) - 32):
        substring = input_string[i:i + 33]
        if len(set(substring)) == 33:
            unique_substrings.add(substring)
    return list(unique_substrings)