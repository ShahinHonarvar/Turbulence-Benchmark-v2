def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    input_string = input_string.lower()
    for i in range(len(input_string)):
        for j in range(i + 84, len(input_string) + 1):
            substring = input_string[i:j]
            if len(substring) == 84 and len(substring) == len(set(substring)):
                substrings.append(substring)
                break
    return substrings