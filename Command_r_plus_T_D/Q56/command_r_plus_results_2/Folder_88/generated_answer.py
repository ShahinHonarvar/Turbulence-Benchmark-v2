def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    for i in range(len(input_string) - 67):
        substring = input_string[i:i + 68]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings