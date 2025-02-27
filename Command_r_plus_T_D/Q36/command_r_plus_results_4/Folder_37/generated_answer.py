def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 45 <= ord(char) < 51:
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)