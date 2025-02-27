def return_nth_smallest_ascii(x):
    return sorted([c for c in x if 29 <= x.index(c) <= 47])[6]