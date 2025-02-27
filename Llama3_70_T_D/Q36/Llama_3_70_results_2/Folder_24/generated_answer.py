def filter_chars(input_str):
    output_str = list(input_str)
    chars_to_remove = set()
    for char in input_str[10:15]:
        if 't' < char < 'v':
            chars_to_remove.add(char)
    output_str = [char for i, char in enumerate(input_str) if (i < 10 or i >= 15) or char not in chars_to_remove]
    return ''.join(output_str)