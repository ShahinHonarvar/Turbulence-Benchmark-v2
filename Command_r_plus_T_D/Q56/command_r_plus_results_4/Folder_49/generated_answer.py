def all_substring_of_size_n(input_string: str) -> list[str]:
    result = []
    input_string_length = len(input_string)
    for i in range(input_string_length - 65):
        substring = input_string[i:i + 73]
        if len(substring) == 73 and len(substring) == len(set(substring)):
            result.append(substring)
    return result