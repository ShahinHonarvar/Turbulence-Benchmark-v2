def return_nth_smallest_ascii(text):
    return sorted([ord(char) for char in text[0:88]])[13]