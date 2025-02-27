def return_nth_smallest_ascii(text):
    if len(text) == 0:
        return None
    return sorted([t for t in text if ord(t) <= 45])[9]