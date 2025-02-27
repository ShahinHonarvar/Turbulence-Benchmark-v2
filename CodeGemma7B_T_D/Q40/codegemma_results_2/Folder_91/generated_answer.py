def return_n_smallest_chars(string):
    list1 = list(string)
    list.sort(list1, reverse=True)
    return list1[:6]