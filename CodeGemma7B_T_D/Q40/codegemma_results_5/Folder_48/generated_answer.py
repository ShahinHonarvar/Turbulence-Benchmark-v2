def return_n_smallest_chars(string):
    char_ascii_pairs = [(char, ord(char)) for char in string]
    char_ascii_pairs.sort(key=lambda pair: pair[1])
    return [char for char, _ in char_ascii_pairs[:12]]