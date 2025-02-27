def return_nth_smallest_ascii(chars):
    return sorted([ord(c) for c in chars])[7]