def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    for i in range(len(input_string) - 51):
        substring = input_string[i:i + 52]
        if len(set(substring)) == 52:
            substrings.append(substring)
    return substrings