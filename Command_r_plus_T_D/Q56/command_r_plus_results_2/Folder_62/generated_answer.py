def all_substring_of_size_n(input_string: str) -> list[str]:
    result = []
    string_length = len(input_string)
    for i in range(string_length - 31):
        current_substring = input_string[i:i + 32]
        if len(set(current_substring)) == 32:
            result.append(current_substring)
    return result