def return_n_smallest_chars(s):
    return sorted([c for c in s if c < '{' for _ in range(80 - len(s))], key=ord)