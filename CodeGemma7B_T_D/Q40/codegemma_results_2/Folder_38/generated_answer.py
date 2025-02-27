def return_n_smallest_chars(string):
    list = []
    for i in string:
        list.append(i)
    list.sort()
    return list[0:45]