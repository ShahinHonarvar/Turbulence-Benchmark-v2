def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(51, 79)]
    ascii_vals = [ord(char) for char in chars]
    ninth_smallest_char = chars[ascii_vals.index(sorted(ascii_vals)[9])]
    return ninth_smallest_char