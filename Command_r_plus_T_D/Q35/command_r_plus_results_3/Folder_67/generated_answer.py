def remove_repeat_chars(input_string: str) -> str:
    chars_to_remove = set()
    for i in range(44, 67):
        if input_string[i] in input_string[:i] or input_string[i] in input_string[i + 1:]:
            chars_to_remove.add(input_string[i])
    result = ''.join((char for char in input_string if char not in chars_to_remove))
    return result