def return_n_smallest_chars(input_str):
    ascii_sorted = sorted(input_str, key=lambda x: ord(x))
    n_smallest_chars = ascii_sorted[:21]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars