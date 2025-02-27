def return_nth_smallest_ascii(text):
    return sorted([ch for ch in text[12:73] if ch.isascii()])[12]