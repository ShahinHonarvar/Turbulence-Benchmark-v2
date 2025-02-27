def all_substring_of_size_n(input_string: str) -> list[str]:
    result = []
    length_of_string = len(input_string)
    for i in range(length_of_string - 49):
        substring = input_string[i:i + 50]
        if len(set(substring)) == 50:
            result.append(substring)
    return result