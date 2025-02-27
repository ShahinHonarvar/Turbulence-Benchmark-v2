def return_n_greatest_chars(string):
    ascii_vals = {char: ord(char) for char in set(string)}
    sorted_chars = sorted(ascii_vals.keys(), key=ascii_vals.get, reverse=True)
    return sorted_chars[:2]