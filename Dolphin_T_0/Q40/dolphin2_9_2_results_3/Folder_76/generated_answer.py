def return_n_smallest_chars(string):
    characters = list(string)
    characters.sort(key=lambda c: ord(c))
    return characters[:3][::-1]