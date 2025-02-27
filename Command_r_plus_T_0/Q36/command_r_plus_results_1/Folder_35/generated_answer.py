def filter_chars(input_string: str) -> str:
    filtered_string = []
    for index, char in enumerate(input_string, start=1):
        if 163 < index < 658 and 40 < ord(char) < 93:
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)