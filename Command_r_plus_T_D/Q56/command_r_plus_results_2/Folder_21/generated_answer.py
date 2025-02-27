def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == 106 and len(substring) == len(set(substring))
    return [substring for substring in input_string if is_substring_valid(substring)]