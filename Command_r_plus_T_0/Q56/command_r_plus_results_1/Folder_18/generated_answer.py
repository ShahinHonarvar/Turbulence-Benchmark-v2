def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == 63 and len(substring) == len(set(substring))
    return list(filter(is_substring_valid, set((input_string[i:i + 63] for i in range(len(input_string))))))