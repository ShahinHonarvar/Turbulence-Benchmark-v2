def all_substring_of_size_n(input_string):
    length = 144
    substrings = []
    for i in range(len(input_string) - length + 1):
        substring = input_string[i:i + length]
        if len(set(substring)) == length:
            substrings.append(substring)
    return substrings if len(set(substrings)) > 0 else []