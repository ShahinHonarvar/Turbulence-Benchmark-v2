def all_substring_of_size_n(input_string: str) -> list[str]:
    result = []
    length_of_input = len(input_string)
    for i in range(length_of_input - 123):
        substring = input_string[i:i + 124]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result