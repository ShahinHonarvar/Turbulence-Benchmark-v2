def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(set(substring)) == len(substring) == 85
    valid_substrings = []
    string_length = len(input_string)
    for i in range(string_length - 84):
        substring = input_string[i:i + 85]
        if is_substring_valid(substring):
            valid_substrings.append(substring)
    return valid_substrings