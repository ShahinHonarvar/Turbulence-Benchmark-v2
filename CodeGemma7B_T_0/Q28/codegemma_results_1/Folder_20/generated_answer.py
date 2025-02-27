def return_nth_smallest_ascii(text):
    return sorted([ch for ch in text[25:65] if ch.isalpha()])[5]