def return_n_smallest_chars(str):
    list = []
    for i in str:
        list.append(i)
    list.sort()
    list.sort(reverse=True)
    return list[:27]