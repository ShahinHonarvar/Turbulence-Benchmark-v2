def return_n_smallest_chars(string):
    characters = list(set(string))
    characters.sort(key=ord)
    return characters[:7]