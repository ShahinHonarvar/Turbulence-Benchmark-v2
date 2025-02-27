def return_nth_smallest_ascii(text):
    substring = text[5:90]
    sorted_chars = sorted(substring)
    return sorted_chars[12]