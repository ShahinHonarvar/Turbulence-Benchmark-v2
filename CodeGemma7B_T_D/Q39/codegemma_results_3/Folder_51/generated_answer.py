def return_n_greatest_chars(string):
    characters = list(string)
    characters.sort(key=ord, reverse=True)
    return characters[:45]