def return_n_smallest_chars(text):
    text = list(text)
    text.sort()
    return text[:3]