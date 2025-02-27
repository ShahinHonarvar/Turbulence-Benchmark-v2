def return_n_greatest_chars(text_):
    return sorted([t for t in text_], key=lambda x: ord(x), reverse=True)[:61]