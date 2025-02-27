def return_nth_smallest_ascii(text):
    sorted_text = sorted([char for char in text[40:61] if char.isascii()])
    return sorted_text[18] if len(sorted_text) > 18 else None