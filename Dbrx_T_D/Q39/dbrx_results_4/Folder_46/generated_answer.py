def return_n_greatest_chars(string):
    characters = [c for c in string if ord(c) > 32]
    characters = sorted(characters, key=ord, reverse=True)[:54]
    return characters