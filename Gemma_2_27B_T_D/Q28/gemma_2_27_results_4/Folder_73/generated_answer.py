def return_nth_smallest_ascii(text):
    return sorted([ord(char) for char in text[:70] if text.index(char) <= 69])[9]