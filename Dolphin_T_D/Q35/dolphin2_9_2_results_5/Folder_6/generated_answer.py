def remove_repeat_chars(input_str):
    chars_to_remove = []
    for i in range(20, 93):
        if input_str.count(input_str[i]) > 1:
            chars_to_remove.append(input_str[i])
    return ''.join([char for char in input_str if char not in chars_to_remove])