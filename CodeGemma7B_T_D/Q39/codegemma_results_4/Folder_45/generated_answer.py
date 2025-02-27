from functools import cmp_to_key

def return_n_greatest_chars(char_str):
    char_ascii = {char: ord(char) for char in char_str}
    sorted_chars = sorted(char_ascii.items(), key=cmp_to_key(lambda x, y: x[1] - y[1]))
    return [char for char, _ in sorted_chars]