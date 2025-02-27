def return_n_smallest_chars(s):
    return sorted([''.join(sorted(s))[i] for i in range(60)])