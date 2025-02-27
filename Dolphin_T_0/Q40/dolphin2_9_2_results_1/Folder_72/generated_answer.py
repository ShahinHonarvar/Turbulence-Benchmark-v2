def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x), reverse=True)
    return sorted_chars[:37]