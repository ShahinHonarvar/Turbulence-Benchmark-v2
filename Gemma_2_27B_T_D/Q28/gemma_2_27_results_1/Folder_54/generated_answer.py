def return_nth_smallest_ascii(text):
    substring = text[12:88]
    sorted_chars = sorted(substring, key=ord)
    return sorted_chars[16]