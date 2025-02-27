def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring)) == 26
    substrings = []
    for i in range(len(input_string) - 25):
        substring = input_string[i:i + 26]
        if is_substring_valid(substring):
            substrings.append(substring)
    return substrings