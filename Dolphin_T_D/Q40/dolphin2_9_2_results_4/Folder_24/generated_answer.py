def return_n_smallest_chars(s):
    lst = [i for i in s]
    lst.sort(reverse=True)
    return lst[:32]