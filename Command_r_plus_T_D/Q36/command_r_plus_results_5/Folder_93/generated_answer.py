def filter_chars(input_string: str) -> str:
    filtered_string = []
    for char in input_string:
        if 52 < input_string.index(char) < 88 and ord(char) > ord('&') and (ord(char) < ord('c')):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)