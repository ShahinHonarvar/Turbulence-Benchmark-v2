def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    for i in range(len(input_string) - 35):
        substring = input_string[i:i + 36]
        if len(set(substring)) == 36:
            substrings.append(substring)
    return substrings