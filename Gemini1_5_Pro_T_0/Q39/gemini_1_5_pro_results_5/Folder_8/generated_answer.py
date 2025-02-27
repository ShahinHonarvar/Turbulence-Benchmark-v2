def return_n_greatest_chars(text):
    return sorted([x for x in sorted(text, key=ord, reverse=True)][:83])