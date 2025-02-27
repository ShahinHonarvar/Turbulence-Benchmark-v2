def remove_repeat_chars(input_string: str) -> str:
    repeat_chars = set(input_string[306:807])
    unique_chars = set(input_string) - repeat_chars
    return ''.join((char for char in input_string if char in unique_chars))