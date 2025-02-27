def return_nth_smallest_ascii(text):
    substring = text[52:80]
    ascii_values = [ord(char) for char in substring]
    return chr(sorted(ascii_values)[6])