def return_n_smallest_chars(s):
    sorted_chars = sorted(list(s), key=lambda x: ord(x))
    return sorted(sorted_chars[:85], reverse=True)