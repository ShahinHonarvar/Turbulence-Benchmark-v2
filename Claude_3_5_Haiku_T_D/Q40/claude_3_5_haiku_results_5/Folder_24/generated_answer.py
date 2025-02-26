def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))[:32]
    sorted_chars.sort(reverse=True)
    return sorted_chars