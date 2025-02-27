def return_n_smallest_chars(string):
    chars = sorted(list(set(string)))[:21]
    chars.sort(reverse=True)
    return chars