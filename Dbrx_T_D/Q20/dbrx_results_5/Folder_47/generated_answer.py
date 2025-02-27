def find_n_th_smallest_num(numbers):
    if len(numbers) < 82:
        return None
    sublist = sorted(numbers[50:82])
    if len(sublist) >= 6:
        return sublist[5]
    else:
        return None