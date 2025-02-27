def remove_repeat_chars(input_string: str) -> str:
    chars_to_remove = set(input_string[38:52])
    for char in chars_to_remove:
        if input_string[38:52].count(char) > 1:
            input_string = input_string.replace(char, '', input_string[38:52].count(char))
    return input_string