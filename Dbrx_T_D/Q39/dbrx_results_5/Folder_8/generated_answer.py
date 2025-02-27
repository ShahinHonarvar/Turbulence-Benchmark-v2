def return_n_greatest_chars(string):
    characters = list(set(string))
    characters.sort(key=ord)
    return characters[-83:]