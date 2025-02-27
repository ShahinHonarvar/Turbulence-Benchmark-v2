def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring)) == 75
    valid_substrings = []
    for i in range(len(input_string) - 74):
        substring = input_string[i:i + 75]
        if is_substring_valid(substring):
            valid_substrings.append(substring)
    return valid_substrings