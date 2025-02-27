def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    length_of_input = len(input_string)
    for i in range(length_of_input - 116):
        current_substring = input_string[i:i + 117]
        if len(set(current_substring)) == 117:
            substrings.append(current_substring)
    return substrings