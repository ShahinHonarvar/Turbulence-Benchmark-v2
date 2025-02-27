def remove_repeat_chars(input_string: str) -> str:
    repeat_chars = set(input_string[57:85])
    repeat_chars = {char for char in repeat_chars if input_string.count(char) > 1}
    return ''.join((char for char in input_string if char not in repeat_chars))