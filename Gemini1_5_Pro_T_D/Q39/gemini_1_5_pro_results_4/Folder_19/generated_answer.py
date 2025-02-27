def return_n_greatest_chars(text):
    return sorted([x for x in text if ord(x) >= ord(sorted(text)[len(text) - 58])])