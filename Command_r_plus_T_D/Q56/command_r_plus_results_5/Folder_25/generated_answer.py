def all_substring_of_size_n(input_string: str) -> list[str]:
    result = []
    for i in range(len(input_string) - 66):
        substring = input_string[i:i + 67]
        if len(set(substring)) == 67:
            result.append(substring)
    return result