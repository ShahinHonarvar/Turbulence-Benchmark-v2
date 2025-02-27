def return_n_smallest_chars(s):
    return sorted([char for char in sorted(s)[:11]], reverse=True)