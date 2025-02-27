def remove_repeat_chars(input_string: str) -> str:
    repeat_chars = set(input_string[200:203])
    repeat_chars = repeat_chars.intersection(set(input_string[:200]))
    return ''.join((char for char in input_string if char not in repeat_chars))