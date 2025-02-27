def filter_chars(input_string: str) -> str:
    filtered_string = []
    for index, char in enumerate(input_string, start=0):
        if 379 <= index <= 898 and 'M' <= char <= 'v':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)