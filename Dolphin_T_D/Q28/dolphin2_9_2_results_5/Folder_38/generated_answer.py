def return_nth_smallest_ascii(s):
    return sorted(s[:46], key=lambda c: ord(c))[9]