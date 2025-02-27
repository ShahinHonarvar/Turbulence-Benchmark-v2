def return_nth_smallest_ascii(chars):
    return sorted(chars, key=ord)[-6]