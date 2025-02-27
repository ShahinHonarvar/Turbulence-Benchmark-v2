def return_nth_smallest_ascii(text):
    ascending_codes = sorted((ord(char) for char in text[0:46]))
    return chr(ascending_codes[9])