def return_nth_smallest_ascii(s):
    chars = sorted(s[3:27])
    ascii_vals = sorted([ord(c) for c in chars])
    fifth_smallest_ascii_val = ascii_vals[4]
    for char in chars:
        if ord(char) == fifth_smallest_ascii_val:
            return char