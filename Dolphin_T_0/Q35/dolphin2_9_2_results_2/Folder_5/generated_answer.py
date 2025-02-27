def remove_repeat_chars(input_str):
    chars_to_remove = set()
    for i in range(2, 8):
        if input_str.count(input_str[i]) > 1:
            chars_to_remove.add(input_str[i])
    for char in chars_to_remove:
        input_str = input_str.replace(char, '')
    return input_str