def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring))
    n = 144
    input_string_length = len(input_string)
    substrings = []
    for i in range(input_string_length - n + 1):
        substring = input_string[i:i + n]
        if is_substring_valid(substring):
            substrings.append(substring)
    return substrings