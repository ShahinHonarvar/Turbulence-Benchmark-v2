def return_nth_smallest_ascii(text):
    text = text[46:82]
    return sorted(text, key=ord)[15]