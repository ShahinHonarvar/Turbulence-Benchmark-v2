def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring))
    substrings_of_size_33 = [input_string[i:i + 33] for i in range(len(input_string) - 32)]
    valid_substrings = [substring for substring in substrings_of_size_33 if is_substring_valid(substring)]
    return valid_substrings