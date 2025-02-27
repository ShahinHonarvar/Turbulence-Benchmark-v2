def filter_chars(input_string: str) -> str:
    chars_to_remove = []
    for char in input_string[11:46]:
        if '!' < char < 'A':
            chars_to_remove.append(char)
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string