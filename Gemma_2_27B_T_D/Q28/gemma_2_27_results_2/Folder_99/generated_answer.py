def return_nth_smallest_ascii(text):
    substring = text[17:66]
    sorted_chars = sorted(substring, key=ord)
    return sorted_chars[7]