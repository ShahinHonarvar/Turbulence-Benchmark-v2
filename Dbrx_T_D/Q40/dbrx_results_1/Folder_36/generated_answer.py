def return_n_smallest_chars(s):
    ascii_chars = [ord(char) for char in s]
    ascii_chars.sort()
    n_smallest_chars = [chr(char) for char in ascii_chars[:32]]
    return n_smallest_chars