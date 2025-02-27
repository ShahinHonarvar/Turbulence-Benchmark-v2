def return_n_smallest_chars(chars):
    return sorted([chr(i) for i in range(ord(chars[0]), ord(chars[-1]) + 1)])[:58]