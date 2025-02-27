def filter_chars(input_string: str) -> str:
    chars_to_remove = []
    for char in input_string[78:81]:
        if 'S' < char < '[':
            chars_to_remove.append(char)
    result = ''.join((char for char in input_string if char not in chars_to_remove))
    return result