def return_n_smallest_chars(s):
    return sorted([c for c in sorted(s)[:61]], reverse=True)