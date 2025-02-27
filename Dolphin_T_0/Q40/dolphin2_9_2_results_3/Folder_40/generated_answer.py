def return_n_smallest_chars(s):
    list_ = list(s)
    list_.sort(key=lambda x: ord(x))
    return list_[:7][::-1]