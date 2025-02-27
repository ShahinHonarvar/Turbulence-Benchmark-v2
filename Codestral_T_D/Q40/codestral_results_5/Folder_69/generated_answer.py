def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    if len(sorted_chars) >= 65:
        return sorted(sorted_chars[:65], reverse=True)
    else:
        return sorted(sorted_chars, reverse=True)