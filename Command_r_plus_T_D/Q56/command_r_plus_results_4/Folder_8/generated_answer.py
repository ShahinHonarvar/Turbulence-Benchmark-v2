def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    for i in range(len(input_string) - 29):
        substring = input_string[i:i + 30]
        if len(set(substring)) == 30:
            substrings.append(substring)
    return substrings