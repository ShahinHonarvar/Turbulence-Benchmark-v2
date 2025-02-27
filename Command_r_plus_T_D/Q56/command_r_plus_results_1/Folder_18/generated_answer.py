def all_substring_of_size_n(input_string: str) -> list[str]:
    result = []
    input_string_length = len(input_string)
    for i in range(input_string_length - 52):
        substring = input_string[i:i + 63]
        if len(substring) == 63 and len(set(substring)) == 63:
            result.append(substring)
    return result