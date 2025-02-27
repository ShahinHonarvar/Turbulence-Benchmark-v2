def return_n_smallest_chars(input_str):
    n = 88
    if len(input_str) < n:
        n = len(input_str)
    sorted_chars = sorted(input_str, key=lambda c: -ord(c))
    return sorted_chars[:n]