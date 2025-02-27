def find_n_th_smallest_num(numbers):
    sublist = numbers[213:323]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) >= 8:
        return sorted_sublist[7]
    else:
        return None