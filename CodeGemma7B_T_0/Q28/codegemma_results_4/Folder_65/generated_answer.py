def return_nth_smallest_ascii(text):
    return sorted([ch for ch in text[32:68] if ch.isalpha()])[11]