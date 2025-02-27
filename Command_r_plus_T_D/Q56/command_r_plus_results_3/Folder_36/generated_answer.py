def all_substring_of_size_n(input_string: str) -> list[str]:

    def is_substring_valid(substring: str) -> bool:
        return len(substring) == len(set(substring))
    input_string = input_string.lower()
    substrings = []
    length = len(input_string)
    for i in range(length):
        for j in range(i + 146, length + 1):
            substring = input_string[i:j]
            if len(substring) == 146 and is_substring_valid(substring):
                substrings.append(substring)
    return substrings