def all_substring_of_size_n(input_string: str) -> list[str]:
    result = []
    string_length = len(input_string)
    for i in range(string_length - 66):
        substring = input_string[i:i + 67]
        if len(substring) == 67 and len(set(substring)) == 67:
            result.append(substring)
    return result