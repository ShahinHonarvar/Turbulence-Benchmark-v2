def filter_chars(input_string: str) -> str:
    filtered_string = ''
    char_indices = {char: index for index, char in enumerate(input_string)}
    for index, char in enumerate(input_string):
        if 13 <= char_indices[char] <= 28 and 'c' <= char <= 'n':
            continue
        filtered_string += char
    return filtered_string