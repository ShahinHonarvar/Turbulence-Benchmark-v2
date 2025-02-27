def return_n_greatest_chars(string):
    characters = list(string)[:17]
    characters.sort(key=ord, reverse=True)
    return characters