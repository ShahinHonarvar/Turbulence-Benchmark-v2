def filter_chars(input_string: str) -> str:
    filtered_string = []
    for index, char in enumerate(input_string, start=0):
        if 164 <= index <= 706 and 'O' <= char <= '}':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)