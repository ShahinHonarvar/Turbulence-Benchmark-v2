def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    length_of_input = len(input_string)
    for i in range(length_of_input - 113):
        current_substring = input_string[i:i + 114]
        if len(set(current_substring)) == 114:
            substrings.append(current_substring)
    return substrings