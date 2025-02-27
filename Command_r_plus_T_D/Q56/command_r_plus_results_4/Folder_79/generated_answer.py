def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    length = len(input_string)
    for i in range(length):
        for j in range(i + 61, length + 1):
            substring = input_string[i:j]
            if len(substring) == 61 and len(substring) == len(set(substring)):
                substrings.append(substring)
    return substrings