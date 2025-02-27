def return_n_greatest_chars(string):
    characters = list(string)
    sorted_chars = sorted(characters, key=ord, reverse=True)
    n_greatest_chars = sorted_chars[:64]
    return n_greatest_chars