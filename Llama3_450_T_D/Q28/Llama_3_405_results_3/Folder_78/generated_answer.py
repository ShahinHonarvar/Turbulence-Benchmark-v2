def return_nth_smallest_ascii(s):
    chars = sorted([char for i, char in enumerate(s[:88])])
    return chars[13]