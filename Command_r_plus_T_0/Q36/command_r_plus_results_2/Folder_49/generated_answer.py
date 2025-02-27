def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 46 < ord(char) < 91 and ord('D') < ord(char) < ord('H'):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)