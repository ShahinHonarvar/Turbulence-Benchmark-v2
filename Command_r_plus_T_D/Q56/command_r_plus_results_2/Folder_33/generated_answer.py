def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    length_of_input = len(input_string)
    for i in range(length_of_input):
        for j in range(i + 105, length_of_input + 1):
            substring = input_string[i:j]
            if len(substring) == 105 and len(substring) == len(set(substring)):
                substrings.append(substring)
    return substrings