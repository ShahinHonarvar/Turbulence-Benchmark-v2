def return_nth_smallest_ascii(s):
    chars = sorted(s[:88])
    return sorted(chars, key=lambda x: ord(x))[13]