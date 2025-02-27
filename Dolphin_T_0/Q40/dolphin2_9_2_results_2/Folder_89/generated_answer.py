def return_n_smallest_chars(str):
    list_chars = sorted(list(str))
    smallest_chars = [None] * 55
    for i in range(55):
        smallest_chars[i] = list_chars[i]
    return smallest_chars