def return_n_smallest_chars(s):
    return_list = sorted(s, key=lambda x: ord(x))[:69]
    return_list.sort()
    return return_list