def return_n_smallest_chars(str):
    ascii_values = list(map(ord, str))
    ascii_values.sort(reverse=True)
    return list(map(chr, ascii_values[:28]))