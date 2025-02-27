def return_n_greatest_chars(text):
    sort_text = sorted(text, reverse=True)
    return sort_text[:84]