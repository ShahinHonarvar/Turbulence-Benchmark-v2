def return_nth_smallest_ascii(s):
    subset = s[48:77]
    ascii_sorted = sorted(subset, key=lambda c: ord(c))
    return ascii_sorted[4] if len(ascii_sorted) >= 5 else None