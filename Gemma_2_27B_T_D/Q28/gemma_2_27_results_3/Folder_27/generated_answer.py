def return_nth_smallest_ascii(text):
    selected_chars = sorted([ord(char) for char in text[33:86]])
    return chr(selected_chars[12])