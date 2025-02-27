def return_nth_smallest_ascii(text):
    return sorted([char for char in text[5:48] if char.isascii()])[12]