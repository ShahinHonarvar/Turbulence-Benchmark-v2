def return_nth_smallest_ascii(text):
    subset = sorted([ord(char) for char in text[6:59]])
    return chr(subset[18])