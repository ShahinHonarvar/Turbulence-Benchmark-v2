def return_nth_smallest_ascii(s):
    return sorted(s[:8], key=lambda c: ord(c))[7]