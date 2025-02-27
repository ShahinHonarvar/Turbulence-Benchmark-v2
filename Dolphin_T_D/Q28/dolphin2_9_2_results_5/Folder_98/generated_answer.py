def return_nth_smallest_ascii(s):
    return sorted(s[:9], key=lambda x: ord(x))[8]