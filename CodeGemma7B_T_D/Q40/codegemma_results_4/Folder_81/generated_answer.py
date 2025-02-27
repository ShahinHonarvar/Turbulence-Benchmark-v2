def return_n_smallest_chars(string):
    list = []
    for i in range(len(string)):
        list.append(string[i])
    list.sort()
    return list[:64]