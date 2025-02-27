def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    length_of_input_string = len(input_string)
    for i in range(length_of_input_string - 56):
        substring = input_string[i:i + 57]
        if len(set(substring)) == 57:
            substrings.append(substring)
    return substrings