def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(set(substring)) == len(substring) and len(substring) == 63
    valid_substrings = []
    for i in range(len(input_string) - 62):
        substring = input_string[i:i + 63]
        if is_substring_valid(substring):
            valid_substrings.append(substring)
    return valid_substrings