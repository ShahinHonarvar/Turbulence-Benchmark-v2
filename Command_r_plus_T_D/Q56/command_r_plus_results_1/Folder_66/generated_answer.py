def all_substring_of_size_n(input_string: str) -> list[str]:
    result = []
    length_input = len(input_string)
    for i in range(length_input - 25):
        substring = input_string[i:i + 26]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result