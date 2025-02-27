def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    length_input = len(input_string)
    for i in range(length_input - 38):
        current_substring = input_string[i:i + 39]
        if len(set(current_substring)) == 39:
            substrings.append(current_substring)
    return substrings