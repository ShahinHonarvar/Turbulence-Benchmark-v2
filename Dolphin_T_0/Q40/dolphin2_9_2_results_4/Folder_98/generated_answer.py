def return_n_smallest_chars(s):
    sorted_chars = sorted([ch for ch in s], key=lambda x: ord(x))
    return sorted(sorted_chars[:68], key=lambda x: ord(x), reverse=True)