def remove_repeat_chars(str_input):
    unique_chars = set()
    output_str = ''
    for i, char in enumerate(str_input):
        if i < 11 or i >= 76:
            continue
        if char not in unique_chars:
            output_str += char
            unique_chars.add(char)
    return output_str