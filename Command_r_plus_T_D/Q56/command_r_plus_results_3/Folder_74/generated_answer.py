def all_substring_of_size_n(input_string: str) -> list[str]:
    result = []
    input_string_length = len(input_string)
    for i in range(input_string_length - 96):
        substring = input_string[i:i + 97]
        if len(set(substring)) == 97:
            result.append(substring)
    return result