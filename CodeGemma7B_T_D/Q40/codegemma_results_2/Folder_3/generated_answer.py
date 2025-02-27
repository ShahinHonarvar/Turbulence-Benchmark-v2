def return_n_smallest_chars(chart):
    return sorted(chart, key=ord, reverse=True)[:28]