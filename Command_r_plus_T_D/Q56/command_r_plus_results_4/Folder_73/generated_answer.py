def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    length_of_input = len(input_string)
    for i in range(length_of_input - 19):
        current_substring = input_string[i:i + 20]
        if len(set(current_substring)) == 20:
            substrings.append(current_substring)
    return substrings