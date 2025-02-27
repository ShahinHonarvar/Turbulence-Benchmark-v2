def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring)) and len(substring) == 142
    return [substring for substring in input_string if is_substring_valid(substring)]