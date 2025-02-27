def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    return sorted([*set(sorted_chars[:87])], key=lambda x: ord(x), reverse=True)