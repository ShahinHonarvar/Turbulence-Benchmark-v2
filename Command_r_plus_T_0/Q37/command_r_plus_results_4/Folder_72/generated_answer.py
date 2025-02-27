def filter_chars(input_string: str) -> str:
    filtered_string = []
    for index, char in enumerate(input_string):
        if 35 <= index <= 51 and 'H' <= char <= 's':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)