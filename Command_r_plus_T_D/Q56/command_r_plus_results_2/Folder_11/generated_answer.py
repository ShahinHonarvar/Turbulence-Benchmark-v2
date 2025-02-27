def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    input_string_length = len(input_string)
    for i in range(input_string_length):
        for j in range(i + 78, input_string_length + 1):
            substring = input_string[i:j]
            if len(substring) == 78 and len(substring) == len(set(substring)):
                substrings.append(substring)
    return substrings