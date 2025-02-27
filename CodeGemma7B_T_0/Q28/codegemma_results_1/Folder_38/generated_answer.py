def return_nth_smallest_ascii(text):
    return sorted([ch for ch in text[0:46] if ch.isalpha()])[9]