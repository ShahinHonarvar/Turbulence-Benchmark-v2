def return_nth_smallest_ascii(text):
    selected_chars = text[51:89 + 1]
    sorted_chars = sorted(selected_chars, key=ord)
    return sorted_chars[13]