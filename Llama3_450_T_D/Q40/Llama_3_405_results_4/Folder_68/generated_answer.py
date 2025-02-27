def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    smallest_89_chars = sorted_chars[:89]
    result = sorted(smallest_89_chars, reverse=True)
    return result