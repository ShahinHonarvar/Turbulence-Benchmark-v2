def all_substring_of_size_n(input_string: str) -> list[str]:
    result = []
    input_string_length = len(input_string)
    for i in range(input_string_length - 49):
        substring = input_string[i:i + 50]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result