def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    length_of_input = len(input_string)
    for i in range(length_of_input - 66):
        substring = input_string[i:i + 74]
        if len(substring) == 74 and len(set(substring)) == 74:
            substrings.append(substring)
    return substrings