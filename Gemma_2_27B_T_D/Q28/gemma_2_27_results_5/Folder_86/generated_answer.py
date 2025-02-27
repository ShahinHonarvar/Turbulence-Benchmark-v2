def return_nth_smallest_ascii(text):
    subset = sorted([ord(char) for char in text[44:70]])
    return chr(subset[14])