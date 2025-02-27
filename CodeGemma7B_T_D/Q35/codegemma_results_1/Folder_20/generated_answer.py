def remove_repeat_chars(input_str):
    output_str = ''
    seen_chars = set()
    for char in input_str[27:96]:
        if char not in seen_chars:
            seen_chars.add(char)
            output_str += char
    return output_str