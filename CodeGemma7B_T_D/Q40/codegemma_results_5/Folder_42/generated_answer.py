def return_n_smallest_chars(str):
    chars = sorted(str, key=ord)[:59]
    chars.sort(reverse=True)
    return chars