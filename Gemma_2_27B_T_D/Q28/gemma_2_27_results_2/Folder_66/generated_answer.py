def return_nth_smallest_ascii(text):
    substring = text[35:53]
    sorted_ascii = sorted([ord(char) for char in substring])
    return chr(sorted_ascii[9])