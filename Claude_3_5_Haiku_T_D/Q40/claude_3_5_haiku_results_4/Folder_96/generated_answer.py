def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s), key=lambda x: ord(x))
    return sorted(sorted_chars[:20], reverse=True)