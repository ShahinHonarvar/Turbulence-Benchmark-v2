def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    string_length = len(input_string)
    for i in range(string_length - 30):
        current_substring = input_string[i:i + 31]
        if len(set(current_substring)) == 31:
            substrings.append(current_substring)
    return substrings