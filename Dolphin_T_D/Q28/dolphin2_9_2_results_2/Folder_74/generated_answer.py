def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(1, 32)]
    ascii_vals = [ord(c) for c in chars]
    return chr(sorted(ascii_vals)[5])