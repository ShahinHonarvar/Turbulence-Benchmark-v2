def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    smallest_chars = sorted_chars[:89]
    result = sorted(smallest_chars, reverse=True)
    return result