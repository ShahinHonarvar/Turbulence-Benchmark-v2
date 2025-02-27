def return_n_greatest_chars(str):
    return sorted([c for c in str], key=ord, reverse=True)[:2]