def return_n_smallest_chars(s):
    sorted_chars = sorted([c for c in s], key=lambda x: ord(x))
    return sorted(sorted_chars[:82], key=lambda x: ord(x), reverse=True)