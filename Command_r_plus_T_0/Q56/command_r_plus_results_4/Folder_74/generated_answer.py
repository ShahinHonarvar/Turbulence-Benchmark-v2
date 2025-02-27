def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == 97 and len(set(substring)) == 97
    valid_substrings = []
    for i in range(len(input_string) - 96):
        substring = input_string[i:i + 97]
        if is_substring_valid(substring):
            valid_substrings.append(substring)
    return valid_substrings