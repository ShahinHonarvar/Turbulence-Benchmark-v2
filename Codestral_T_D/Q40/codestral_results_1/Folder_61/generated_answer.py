def return_n_smallest_chars(s):
    sorted_chars = sorted(s)[:66]
    sorted_chars.sort(reverse=True)
    return sorted_chars