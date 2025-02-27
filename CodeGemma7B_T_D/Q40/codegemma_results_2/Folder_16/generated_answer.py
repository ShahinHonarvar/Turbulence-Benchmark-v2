def return_n_smallest_chars(s):
    s += s * (64 // len(s))
    return sorted(list(set(s))[:64], reverse=True)