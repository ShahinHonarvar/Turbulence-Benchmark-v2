def return_nth_smallest_ascii(text):
    sub_text = text[46:83]
    sorted_chars = sorted(sub_text, key=ord)
    return sorted_chars[15]