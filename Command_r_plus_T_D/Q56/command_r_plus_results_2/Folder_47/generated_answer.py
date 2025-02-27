def all_substring_of_size_n(input_string: str) -> list[str]:
    result = []
    for i in range(len(input_string) - 90):
        substring = input_string[i:i + 91]
        if len(set(substring)) == 91:
            result.append(substring)
    return result