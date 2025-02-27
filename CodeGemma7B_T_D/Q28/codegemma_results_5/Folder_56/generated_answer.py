def return_nth_smallest_ascii(a):
    return sorted([ord(i) for i in a])[3]