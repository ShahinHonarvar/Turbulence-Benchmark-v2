def all_substring_of_size_n(input_string: str) -> list[str]:
    n = 91
    substrings = []
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings