def return_n_smallest_chars(characters):
    return sorted([c for c in characters], key=ord)[:84]