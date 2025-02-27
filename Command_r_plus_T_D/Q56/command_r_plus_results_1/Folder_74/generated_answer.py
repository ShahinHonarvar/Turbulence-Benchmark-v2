def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    for i in range(len(input_string) - 96):
        substring = input_string[i:i + 97]
        if len(set(substring)) == 97:
            substrings.append(substring)
    return substrings