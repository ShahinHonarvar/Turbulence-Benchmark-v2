def return_n_smallest_chars(string):
    characters = sorted(set(string), key=ord)
    return characters[:88][::-1]