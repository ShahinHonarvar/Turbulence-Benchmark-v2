def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    n_smallest_chars = sorted_chars[:37]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars