def remove_repeat_chars(input_str):
    chars_to_remove = set()
    for i in range(331, 543):
        if i < len(input_str) and input_str.count(input_str[i]) > 1:
            chars_to_remove.add(input_str[i])
    return ''.join((char for char in input_str if char not in chars_to_remove))