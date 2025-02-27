def return_nth_smallest_ascii(s):
    chars = s[36:80]
    ascii_vec = [ord(c) for c in chars]
    ascii_vec.sort()
    return chr(ascii_vec[11])