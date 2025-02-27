def all_substring_of_size_n(input_string: str) -> list[str]:
    substrings = []
    length_of_string = len(input_string)
    for i in range(length_of_string):
        for j in range(i + 114, length_of_string + 1):
            substring = input_string[i:j]
            if len(substring) == 114 and len(substring) == len(set(substring)):
                substrings.append(substring)
                break
    return substrings