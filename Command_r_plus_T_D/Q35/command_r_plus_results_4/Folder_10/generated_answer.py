def remove_repeat_chars(input_string: str) -> str:
    repeat_chars = set(input_string[36:54])
    repeat_chars = repeat_chars.intersection(set(input_string[:36]))
    repeat_chars = repeat_chars.intersection(set(input_string[54:]))
    return ''.join((char for char in input_string if char not in repeat_chars))