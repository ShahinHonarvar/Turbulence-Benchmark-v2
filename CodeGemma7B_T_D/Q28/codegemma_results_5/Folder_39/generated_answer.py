def return_nth_smallest_ascii(arg):
    return sorted([ord(c) for c in arg[1:67] if ord(c) != 90])[7]