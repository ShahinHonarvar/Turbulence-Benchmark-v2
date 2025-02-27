def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    length_of_input = len(input_string)
    for i in range(length_of_input - 46):
        current_substring = input_string[i:i + 47]
        if len(current_substring) == len(set(current_substring)):
            substrings.append(current_substring)
    return substrings