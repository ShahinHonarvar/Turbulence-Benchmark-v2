def return_n_smallest_chars(text):
    characters = sorted([chr(i) for i in range(ord(text[0]), ord(text[-1]) + 1)])
    return characters[:8]