def return_nth_smallest_ascii(text):
    subset = sorted([ord(char) for char in text[47:71]])
    return chr(subset[13])