def all_substring_of_size_n(input_string: str) -> list[str]:
    result = []
    length = len(input_string)
    for i in range(length):
        for j in range(i + 91, length + 1):
            substring = input_string[i:j]
            if len(substring) == 91 and len(substring) == len(set(substring)):
                result.append(substring)
    return result