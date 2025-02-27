def return_nth_smallest_ascii(text):
    substring = text[67:78]
    sorted_chars = sorted(substring, key=ord)
    return sorted_chars[6]