def return_n_greatest_chars(s):
    return sorted([char for char in s if char.isprintable()], key=ord, reverse=True)[:64]