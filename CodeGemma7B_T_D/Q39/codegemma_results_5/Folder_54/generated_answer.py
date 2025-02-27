def return_n_greatest_chars(s):
    char_ascii_pairs = [(char, ord(char)) for char in s]
    char_ascii_pairs.sort(key=lambda x: x[1], reverse=True)
    return [char for char, _ in char_ascii_pairs[:79]]