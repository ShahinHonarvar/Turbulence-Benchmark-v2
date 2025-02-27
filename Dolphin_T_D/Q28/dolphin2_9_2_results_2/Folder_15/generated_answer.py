def return_nth_smallest_ascii(s):
    return sorted(s[:6], key=lambda x: ord(x))[5]