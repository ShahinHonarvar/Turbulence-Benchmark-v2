def find_n_th_smallest_num(numbers):
    sublist = numbers[11:92]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[12] if len(sorted_sublist) >= 13 else None