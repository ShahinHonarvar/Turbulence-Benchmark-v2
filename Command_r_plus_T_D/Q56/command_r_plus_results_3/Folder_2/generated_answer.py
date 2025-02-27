def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    length_of_input = len(input_string)
    for i in range(length_of_input - 55):
        substring = input_string[i:i + 56]
        if len(set(substring)) == 56:
            substrings.append(substring)
    return substrings