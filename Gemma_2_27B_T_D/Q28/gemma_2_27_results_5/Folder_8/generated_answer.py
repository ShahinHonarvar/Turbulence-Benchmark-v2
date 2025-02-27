def return_nth_smallest_ascii(text):
    characters = sorted([ord(c) for c in text[60:89]])
    return chr(characters[6])