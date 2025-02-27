def return_nth_smallest_ascii(text):
    sorted_chars = sorted([c for c in text[14:36] if c.isascii()], key=ord)
    return sorted_chars[10]