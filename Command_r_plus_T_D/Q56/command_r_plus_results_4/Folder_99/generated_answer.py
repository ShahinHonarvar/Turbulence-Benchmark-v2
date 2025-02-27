def all_substring_of_size_n(input_string: str) -> list[str]:
    result = []
    string_length = len(input_string)
    for i in range(string_length):
        for j in range(i + 110, string_length + 1):
            substring = input_string[i:j]
            if len(substring) == 110 and len(substring) == len(set(substring)):
                result.append(substring)
                break
    return result