def return_n_greatest_chars(string):
    characters = sorted(string, key=ord, reverse=True)[:79]
    return characters