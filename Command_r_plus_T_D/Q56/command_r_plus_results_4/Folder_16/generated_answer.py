def all_substring_of_size_n(input_string: str) -> list[str]:
    result = []
    for i in range(len(input_string) - 123):
        substring = input_string[i:i + 124]
        if len(set(substring)) == 124:
            result.append(substring)
    return result