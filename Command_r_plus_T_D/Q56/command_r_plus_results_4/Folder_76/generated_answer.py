def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring))
    n = 149
    valid_substrings = []
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if is_substring_valid(substring):
            valid_substrings.append(substring)
    return valid_substrings