def return_nth_smallest_ascii(text):
    text = text[29:34]
    return min(text, key=ord)