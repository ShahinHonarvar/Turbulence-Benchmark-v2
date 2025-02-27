def return_nth_smallest_ascii(text):
    substr = text[32:68]
    sorted_chars = sorted(substr, key=lambda x: ord(x))
    return sorted_chars[11]