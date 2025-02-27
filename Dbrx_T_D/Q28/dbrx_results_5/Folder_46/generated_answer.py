def return_nth_smallest_ascii(input_string):
    filtered_chars = [char for char in input_string[34:86] if ord(char) > 31 and ord(char) < 127]
    filtered_chars.sort(key=ord)
    return filtered_chars[19] if len(filtered_chars) > 19 else None