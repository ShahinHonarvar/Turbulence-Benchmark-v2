def all_substring_of_size_n(input_string: str) -> list[str]:
    result = []
    length = len(input_string)
    for i in range(length - 53):
        substring = input_string[i:i + 54]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result