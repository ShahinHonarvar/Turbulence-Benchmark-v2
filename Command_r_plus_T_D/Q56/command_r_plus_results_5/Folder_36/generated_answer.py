def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring))
    substrings_of_size_n = []
    for i in range(len(input_string) - 145):
        substring = input_string[i:i + 146]
        if is_substring_valid(substring):
            substrings_of_size_n.append(substring)
    return substrings_of_size_n