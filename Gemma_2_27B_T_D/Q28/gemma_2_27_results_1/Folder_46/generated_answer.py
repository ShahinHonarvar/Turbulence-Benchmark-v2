def return_nth_smallest_ascii(text):
    characters = sorted([ord(char) for char in text[34:86]])
    return chr(characters[19])