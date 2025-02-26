def return_n_smallest_chars(s):
    unique_chars = list(set(s))
    sorted_chars = sorted(unique_chars, key=ord)
    smallest_chars = sorted_chars[:72]
    smallest_chars.extend([''] * (72 - len(smallest_chars)))
    return sorted(smallest_chars, reverse=True)