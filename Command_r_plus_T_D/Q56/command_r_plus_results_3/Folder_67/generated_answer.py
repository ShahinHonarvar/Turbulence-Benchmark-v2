def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    length_of_input = len(input_string)
    for i in range(length_of_input - 42):
        current_substring = input_string[i:i + 43]
        if len(set(current_substring)) == 43:
            substrings.append(current_substring)
    return substrings