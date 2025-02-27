def return_n_smallest_chars(string):
    characters = list(string)
    characters.sort(key=ord)
    return characters[-65:][::-1]