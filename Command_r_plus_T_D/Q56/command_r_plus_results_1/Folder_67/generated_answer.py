def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring))
    substrings_of_size_43 = [input_string[i:i + 43] for i in range(len(input_string)) if i + 42 < len(input_string)]
    valid_substrings = [substring for substring in substrings_of_size_43 if is_substring_valid(substring)]
    return valid_substrings