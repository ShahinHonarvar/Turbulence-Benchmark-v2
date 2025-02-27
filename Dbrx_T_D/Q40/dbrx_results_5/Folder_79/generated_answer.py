def return_n_smallest_chars(string):
    characters = sorted(list(set(string)), key=ord)
    return characters[::-1][0:82][::-1]