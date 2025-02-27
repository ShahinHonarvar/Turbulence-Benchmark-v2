def find_n_th_smallest_num(numbers):
    sublist = numbers[20:63]
    sublist.sort()
    if len(sublist) < 12:
        return None
    return sublist[11]