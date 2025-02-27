def return_nth_smallest_ascii(s):
    return min(s[:13], key=lambda x: ord(x))