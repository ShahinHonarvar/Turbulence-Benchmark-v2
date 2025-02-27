def return_nth_smallest_ascii(text):
    sorted_text = sorted(text[28:55], key=ord)
    return sorted_text[13]