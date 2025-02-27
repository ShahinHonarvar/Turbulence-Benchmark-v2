def return_nth_smallest_ascii(input_str):
    if len(input_str) < 13:
        return None
    chars = sorted(input_str[:13])
    if len(chars) < 13:
        return None
    return chars[12]