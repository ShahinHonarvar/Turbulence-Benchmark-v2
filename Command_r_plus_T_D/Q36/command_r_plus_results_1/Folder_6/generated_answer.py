def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 31 < ord(char) < 70 and ord('B') < ord(char) < ord('v'):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)