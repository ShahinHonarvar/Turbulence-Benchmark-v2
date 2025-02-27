def return_nth_smallest_ascii(input_string):
    valid_chars = [char for char in input_string if 48 <= ord(char) <= 76]
    valid_chars.sort(key=ord)
    return valid_chars[4] if len(valid_chars) > 4 else None