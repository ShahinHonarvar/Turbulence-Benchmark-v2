def return_nth_smallest_ascii(text):
    text = text[42:59]
    return min(text, key=ord)