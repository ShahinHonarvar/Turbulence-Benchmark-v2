def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    for i in range(len(input_string) - 2):
        substring = input_string[i:i + 3]
        if len(set(substring)) == 3:
            substrings.append(substring)
    return substrings