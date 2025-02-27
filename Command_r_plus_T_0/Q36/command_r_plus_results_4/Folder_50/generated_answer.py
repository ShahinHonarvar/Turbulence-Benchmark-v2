def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 61 < ord(char) < 88 and ord(char) > ord('%') and (ord(char) < ord('q')):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)