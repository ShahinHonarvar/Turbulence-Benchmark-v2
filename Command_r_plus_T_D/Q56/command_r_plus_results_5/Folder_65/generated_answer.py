def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    for i in range(len(input_string) - 80):
        substring = input_string[i:i + 81]
        if len(set(substring)) == 81:
            substrings.append(substring)
    return substrings