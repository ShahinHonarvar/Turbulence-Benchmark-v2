def filter_chars(input_str):
    chars_to_remove = [c for c in input_str[52:82] if 'A' <= c <= 'U']
    for char in chars_to_remove:
        input_str = input_str.replace(char, '', 1)
    return input_str