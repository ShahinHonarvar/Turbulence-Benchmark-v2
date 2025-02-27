def return_nth_smallest_ascii(s):
    chars = sorted(set(s[:16]))[:16]
    return chr(chars.index(sorted(chars)[15]))