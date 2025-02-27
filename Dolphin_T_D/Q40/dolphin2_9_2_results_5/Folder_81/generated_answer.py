def return_n_smallest_chars(s):
    return sorted([''.join(sorted(s)) for _ in range(64)])