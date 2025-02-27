def remove_repeat_chars(input_str):
    chars_to_remove = set()
    for i in range(20, 35):
        if input_str.count(input_str[i]) > 1:
            chars_to_remove.add(input_str[i])
    return ''.join([c for c in input_str if c not in chars_to_remove])