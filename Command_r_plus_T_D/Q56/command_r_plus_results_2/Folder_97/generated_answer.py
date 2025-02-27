def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring)) and len(substring) == 142
    return list(filter(is_substring_valid, set((input_string[i:j] for i, j in zip(range(len(input_string)), range(142, len(input_string) + 1))))))