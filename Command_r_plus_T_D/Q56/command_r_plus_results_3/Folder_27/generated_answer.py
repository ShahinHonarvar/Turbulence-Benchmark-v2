def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    length_of_string = len(input_string)
    for i in range(length_of_string - 56):
        substring = input_string[i:i + 57]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings