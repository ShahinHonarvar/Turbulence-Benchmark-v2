def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == 85 and len(set(substring)) == 85
    substrings = []
    for i in range(len(input_string) - 84):
        substring = input_string[i:i + 85]
        if is_substring_valid(substring):
            substrings.append(substring)
    return substrings