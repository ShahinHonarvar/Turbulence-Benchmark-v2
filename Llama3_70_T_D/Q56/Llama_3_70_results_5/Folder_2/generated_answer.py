def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string) - 55):
        substring = input_string[i:i + 56]
        if len(set(substring)) == 56 and substring not in substrings:
            substrings.append(substring)
    return substrings