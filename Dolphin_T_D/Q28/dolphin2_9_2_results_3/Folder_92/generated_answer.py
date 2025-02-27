def return_nth_smallest_ascii(s):
    return sorted(s[:4], key=lambda x: ord(x))[3]