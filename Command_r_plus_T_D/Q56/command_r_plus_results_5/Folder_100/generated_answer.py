def all_substring_of_size_n(input_string: str) -> list[str]:
    result = []
    for i in range(len(input_string) - 91):
        substring = input_string[i:i + 92]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result