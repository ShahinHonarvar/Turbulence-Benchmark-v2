def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    for i in range(len(input_string) - 5):
        substring = input_string[i:i + 6]
        if len(set(substring)) == 6:
            substrings.append(substring)
    return substrings