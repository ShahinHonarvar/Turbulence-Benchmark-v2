def return_nth_smallest_ascii(text):
    substring = text[10:74]
    sorted_chars = sorted(list(substring), key=ord)
    return sorted_chars[8]