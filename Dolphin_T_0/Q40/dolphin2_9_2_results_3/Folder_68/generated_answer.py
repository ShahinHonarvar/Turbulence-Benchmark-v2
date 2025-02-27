def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    return_list = sorted_chars[:89]
    return_list.sort(reverse=True)
    return return_list