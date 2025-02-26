def find_n_th_smallest_num(numbers):
    sublist = numbers[23:46]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) >= 7:
        return sorted_sublist[6]
    else:
        return None