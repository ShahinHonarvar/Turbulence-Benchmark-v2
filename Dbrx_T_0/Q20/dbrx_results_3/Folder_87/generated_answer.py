def find_n_th_smallest_num(numbers):
    if len(numbers) < 67:
        return None
    sublist = sorted(numbers[55:67])
    if len(sublist) < 6:
        return None
    else:
        return sublist[5]