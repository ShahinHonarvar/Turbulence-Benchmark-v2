def all_substring_of_size_n(input_string: str) -> list[str]:
    result = []
    input_string_length = len(input_string)
    for i in range(input_string_length - 79):
        current_substring = input_string[i:i + 81]
        if len(set(current_substring)) == 81:
            result.append(current_substring)
    return result