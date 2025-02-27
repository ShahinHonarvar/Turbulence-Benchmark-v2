def return_nth_smallest_ascii(text):
    substring = text[17:87]
    sorted_chars = sorted(set(substring), key=ord)
    return sorted_chars[14]