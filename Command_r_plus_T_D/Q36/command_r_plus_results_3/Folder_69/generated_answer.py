def filter_chars(input_string: str) -> str:
    filtered_string = []
    for i, char in enumerate(input_string):
        if 343 <= i < 665 and ord(char) > ord('%') and (ord(char) < ord('U')):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)