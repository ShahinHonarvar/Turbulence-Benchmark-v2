def return_nth_smallest_ascii(text):
    if len(text) <= 3:
        return None
    text = text[0:4]
    text.sort()
    return text[0]