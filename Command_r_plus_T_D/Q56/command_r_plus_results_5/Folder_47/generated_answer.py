def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    input_string_length = len(input_string)
    for i in range(input_string_length - 90):
        current_substring = input_string[i:i + 91]
        if len(set(current_substring)) == 91:
            substrings.append(current_substring)
    return substrings