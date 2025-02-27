def filter_chars(input_string: str) -> str:
    filtered_string = ''
    for i, char in enumerate(input_string):
        if i < 12 or i > 77 or (ord(char) < ord(':') or ord(char) > ord('L')):
            filtered_string += char
    return filtered_string