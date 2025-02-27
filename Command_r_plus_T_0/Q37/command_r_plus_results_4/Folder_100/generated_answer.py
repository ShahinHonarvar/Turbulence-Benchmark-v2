def filter_chars(input_string: str) -> str:
    chars_to_remove = set()
    for char in input_string[88:91]:
        if 'J' <= char <= 'Q':
            chars_to_remove.add(char)
    result = ''.join((char for char in input_string if char not in chars_to_remove))
    return result