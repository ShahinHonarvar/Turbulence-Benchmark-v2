def remove_repeat_chars(input_string: str) -> str:
    repeat_chars = set()
    for char in input_string[306:807]:
        if input_string.count(char) > 1:
            repeat_chars.add(char)
    return ''.join((char for char in input_string if char not in repeat_chars))