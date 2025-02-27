def remove_repeat_chars(input_str):
    unique_chars = []
    for char in input_str[1:11]:
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join(unique_chars)