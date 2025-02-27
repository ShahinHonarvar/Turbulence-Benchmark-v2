def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring)) and len(substring) == 130
    valid_substrings = []
    string_length = len(input_string)
    for i in range(string_length):
        for j in range(i + 1, string_length + 1):
            substring = input_string[i:j]
            if len(substring) == 130 and is_substring_valid(substring):
                valid_substrings.append(substring)
    return valid_substrings