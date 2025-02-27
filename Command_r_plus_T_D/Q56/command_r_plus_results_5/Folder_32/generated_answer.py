def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring)) == 71
    substrings = []
    string_length = len(input_string)
    for i in range(string_length - 70):
        for j in range(i + 71, string_length + 1):
            substring = input_string[i:j]
            if is_substring_valid(substring):
                substrings.append(substring)
    return substrings