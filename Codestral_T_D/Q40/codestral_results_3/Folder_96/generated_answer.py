def return_n_smallest_chars(string):
    sorted_chars = sorted(string)[:20]
    sorted_chars.sort(reverse=True)
    return sorted_chars