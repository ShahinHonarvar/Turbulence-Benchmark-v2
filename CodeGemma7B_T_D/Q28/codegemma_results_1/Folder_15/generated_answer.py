def return_nth_smallest_ascii(text):
    text = text[0:6]
    return sorted(set(text))[5]