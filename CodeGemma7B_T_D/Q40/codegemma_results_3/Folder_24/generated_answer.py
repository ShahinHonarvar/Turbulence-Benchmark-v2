def return_n_smallest_chars(char_str):
    sorted(char_str, key=lambda c: ord(c))[:32]