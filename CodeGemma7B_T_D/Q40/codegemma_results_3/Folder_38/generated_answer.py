def return_n_smallest_chars(string):
    char_ascii_pairs = [(char, ord(char)) for char in string]
    char_ascii_pairs.sort(key=lambda pair: pair[1])
    n_smallest_chars = [pair[0] for pair in char_ascii_pairs[:45]]
    return n_smallest_chars