def return_n_smallest_chars(s):
    if len(s) < 39:
        return 'Not enough characters.'
    sorted_chars = sorted(s, key=lambda x: ord(x))
    smallest_chars = sorted_chars[:39]
    smallest_chars.sort(reverse=True)
    return smallest_chars