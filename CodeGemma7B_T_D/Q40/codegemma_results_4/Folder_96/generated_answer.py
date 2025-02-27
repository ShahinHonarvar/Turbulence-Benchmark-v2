def return_n_smallest_chars(given_string):
    ascii_values = sorted(list(map(ord, given_string)), reverse=True)
    return ''.join(map(chr, ascii_values[:20]))