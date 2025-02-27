def all_substring_of_size_n(input_string: str) -> list[str]:

    def get_all_substrings(string, size):
        return [string[i:i + size] for i in range(len(string) - size + 1)]

    def has_unique_chars(substring):
        return len(substring) == len(set(substring))
    substrings = get_all_substrings(input_string, 79)
    unique_substrings = [s for s in substrings if has_unique_chars(s)]
    return unique_substrings