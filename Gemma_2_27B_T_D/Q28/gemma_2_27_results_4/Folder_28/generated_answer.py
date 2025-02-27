def return_nth_smallest_ascii(text):
    substring = text[25:78]
    sorted_chars = sorted(substring, key=ord)
    return sorted_chars[15]