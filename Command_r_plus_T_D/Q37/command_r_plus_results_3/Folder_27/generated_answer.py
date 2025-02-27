def filter_chars(input_string: str) -> str:
    filtered_string = []
    for index, char in enumerate(input_string):
        if 43 <= index <= 80 and '=' <= char <= 'E':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)