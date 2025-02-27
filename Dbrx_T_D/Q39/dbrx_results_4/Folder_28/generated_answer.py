def return_n_greatest_chars(string):
    characters = list(set(string))
    characters.sort(key=lambda char: ord(char))
    return characters[-3:]