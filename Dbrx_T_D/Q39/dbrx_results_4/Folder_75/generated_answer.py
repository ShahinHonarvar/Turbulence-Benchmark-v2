def return_n_greatest_chars(string):
    characters = list(string)
    sorted_chars = sorted(characters, key=ord, reverse=True)[:2]
    return sorted_chars