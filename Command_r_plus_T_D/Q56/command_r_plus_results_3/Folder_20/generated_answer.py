def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    length_of_input = len(input_string)
    for i in range(length_of_input - 49):
        substring = input_string[i:i + 50]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings