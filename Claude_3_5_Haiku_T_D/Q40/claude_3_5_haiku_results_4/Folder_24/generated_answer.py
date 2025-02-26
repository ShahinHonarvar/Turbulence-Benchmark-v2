def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string), key=lambda x: ord(x))
    return sorted(sorted_chars[:32], reverse=True)