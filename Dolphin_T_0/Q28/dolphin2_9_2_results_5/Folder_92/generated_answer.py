def return_nth_smallest_ascii(s):
    return sorted(s[:4], key=ord)[3]