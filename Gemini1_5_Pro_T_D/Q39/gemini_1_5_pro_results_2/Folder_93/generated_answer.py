def return_n_greatest_chars(text):
    return sorted([c for c in text if ord(c) >= ord(sorted(text)[len(text) - 77])], reverse=True)