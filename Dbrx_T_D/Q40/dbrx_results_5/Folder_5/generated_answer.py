def return_n_smallest_chars(string):
    characters = sorted(list(set(string)), reverse=True)
    return characters[:46]