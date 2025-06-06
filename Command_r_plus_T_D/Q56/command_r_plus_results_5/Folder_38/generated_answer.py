def all_substring_of_size_n(input_string: str) -> list[str]:
    result = []
    string_length = len(input_string)
    for i in range(string_length - 34):
        substring = input_string[i:i + 35]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result