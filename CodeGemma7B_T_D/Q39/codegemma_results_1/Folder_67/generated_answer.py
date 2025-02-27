def return_n_greatest_chars(txt):
    return sorted(txt, key=ord, reverse=True)[:66]