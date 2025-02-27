def filter_chars(input_string: str) -> str:
    filtered_string = []
    for index, char in enumerate(input_string):
        if 10 <= index <= 69 and 'I' <= char <= 'K':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)