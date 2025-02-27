def return_n_smallest_chars(str):
    list = []
    for x in str:
        list.append(x)
    list.sort(key=ord, reverse=True)
    return list[:89]