def find_n_th_smallest_num(numbers):
    sublist = numbers[34:95]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) >= 18:
        return sorted_sublist[17]
    else:
        return None