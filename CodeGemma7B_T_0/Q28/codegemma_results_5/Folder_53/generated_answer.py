def return_nth_smallest_ascii(text):
    return sorted([char for char in text[40:61] if char.isascii()])[18]