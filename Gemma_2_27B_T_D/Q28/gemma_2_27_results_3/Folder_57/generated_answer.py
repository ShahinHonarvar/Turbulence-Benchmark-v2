def return_nth_smallest_ascii(text):
    subset = text[17:35]
    sorted_chars = sorted(subset, key=ord)
    return sorted_chars[17]