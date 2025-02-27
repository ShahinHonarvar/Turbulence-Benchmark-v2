def return_nth_smallest_ascii(text):
    substring = text[29:34]
    sorted_chars = sorted(substring, key=ord)
    return sorted_chars[4]