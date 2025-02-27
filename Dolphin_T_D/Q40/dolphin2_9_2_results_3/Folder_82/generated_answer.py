def return_n_smallest_chars(s):
    return sorted(s, key=lambda x: x.encode('utf-8'))[:60]