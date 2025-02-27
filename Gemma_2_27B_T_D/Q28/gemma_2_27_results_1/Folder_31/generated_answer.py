def return_nth_smallest_ascii(text):
    substring = text[10:83]
    sorted_chars = sorted(substring)
    return sorted_chars[17]