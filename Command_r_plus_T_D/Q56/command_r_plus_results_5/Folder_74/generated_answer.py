def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == 97 and len(set(substring)) == 97
    return [substring for substring in input_string if is_substring_valid(substring)]