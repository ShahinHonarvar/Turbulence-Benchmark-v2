def all_substring_of_size_n(input_string: str) -> list[str]:
    result = []
    for i in range(len(input_string) - 89):
        substring = input_string[i:i + 90]
        if len(set(substring)) == 90:
            result.append(substring)
    return result