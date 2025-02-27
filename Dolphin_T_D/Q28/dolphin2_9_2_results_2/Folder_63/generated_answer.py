def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(47, 71) if s[i].isalpha() and len(set(s[47:71])) == len(s[47:71])]
    ascii_vals = [ord(c) for c in chars]
    nth_smallest = sorted(ascii_vals)[13]
    return chr(nth_smallest)