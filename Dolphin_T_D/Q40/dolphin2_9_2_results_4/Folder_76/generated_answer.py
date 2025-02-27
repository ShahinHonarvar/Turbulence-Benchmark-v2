def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    return sorted(sorted_chars[:3], reverse=True)