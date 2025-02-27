def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    length_of_input_string = len(input_string)
    for i in range(length_of_input_string - 93):
        current_substring = input_string[i:i + 94]
        if len(set(current_substring)) == 94:
            substrings.append(current_substring)
    return substrings