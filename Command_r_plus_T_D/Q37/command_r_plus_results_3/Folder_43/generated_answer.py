def filter_chars(input_string: str) -> str:
    filtered_string = []
    for index, char in enumerate(input_string, start=0):
        if 'W' <= char <= '{' and 15 <= index <= 55:
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)