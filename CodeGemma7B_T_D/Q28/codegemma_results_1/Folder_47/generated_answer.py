def return_nth_smallest_ascii(string):
    return sorted([c for c in string[3:53] if c in string])[7]