def all_substring_of_size_n(input_string: str) -> list[str]:
    result = []
    input_string_length = len(input_string)
    for i in range(input_string_length):
        for j in range(i + 25, input_string_length + 1):
            substring = input_string[i:j]
            if len(substring) == 25 and len(substring) == len(set(substring)):
                result.append(substring)
    return result