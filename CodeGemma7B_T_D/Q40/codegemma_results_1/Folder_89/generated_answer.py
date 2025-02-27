def return_n_smallest_chars(str):
    list = []
    for char in str:
        list.append(char)
    list.sort()
    return list[:55]