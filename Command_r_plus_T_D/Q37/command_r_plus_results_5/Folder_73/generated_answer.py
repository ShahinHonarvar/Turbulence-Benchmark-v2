def filter_chars(input_string: str) -> str:
    filtered_string = []
    for index, char in enumerate(input_string):
        if 22 <= index <= 85 and '7' <= char <= 'e':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)