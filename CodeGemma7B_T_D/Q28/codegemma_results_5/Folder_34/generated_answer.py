def return_nth_smallest_ascii(text):
    text = text[0:19]
    return min(text, key=ord)