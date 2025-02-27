def return_nth_smallest_ascii(input_str: str) -> str:
    ascii_values = sorted((ord(c) for c in input_str[28:68] if 28 <= input_str.index(c) <= 67))
    if len(ascii_values) >= 15:
        return chr(ascii_values[14])
    else:
        return ''