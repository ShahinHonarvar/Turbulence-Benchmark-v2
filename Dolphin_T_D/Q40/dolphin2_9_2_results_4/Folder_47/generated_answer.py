def return_n_smallest_chars(ed_string):
    list_chars = list(ed_string)
    list_chars.sort(key=lambda x: ord(x))
    return list_chars[:21][::-1]