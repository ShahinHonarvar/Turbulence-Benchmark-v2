def return_n_greatest_chars(characters):
    return sorted([c for c in characters], key=ord, reverse=True)[:69]