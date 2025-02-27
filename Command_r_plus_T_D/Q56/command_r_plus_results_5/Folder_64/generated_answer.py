def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    string_length = len(input_string)
    for i in range(string_length):
        for j in range(i + 8, string_length + 1):
            substring = input_string[i:j]
            if len(substring) == 8 and len(substring) == len(set(substring)):
                substrings.append(substring)
    return substrings