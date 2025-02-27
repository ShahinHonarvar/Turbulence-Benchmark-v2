def remove_repeat_chars(input_string: str) -> str:
    repeat_chars = set(input_string[30:200])
    repeat_chars = set([char for char in repeat_chars if input_string.count(char) > 1])
    return ''.join([char for char in input_string if char not in repeat_chars])