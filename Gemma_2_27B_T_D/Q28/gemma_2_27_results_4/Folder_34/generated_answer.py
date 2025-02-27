def return_nth_smallest_ascii(text):
    return chr(sorted([ord(c) for c in text[:19]])[18])