def return_nth_smallest_ascii(text):
    substring = text[60:89]
    sorted_chars = sorted(substring, key=ord)
    return sorted_chars[6]