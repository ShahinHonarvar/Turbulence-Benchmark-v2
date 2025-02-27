def filter_chars(input_string: str) -> str:
    filtered_string = list(input_string)
    for idx in range(56, 86):
        char = input_string[idx]
        if '+' < char < 'w':
            filtered_string.remove(char)
    return ''.join(filtered_string)