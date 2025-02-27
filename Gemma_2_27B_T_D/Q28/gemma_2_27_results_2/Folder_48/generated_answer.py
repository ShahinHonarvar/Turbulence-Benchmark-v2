def return_nth_smallest_ascii(text):
    subset = text[37:60]
    sorted_chars = sorted(subset, key=ord)
    return sorted_chars[5]