def find_n_th_smallest_num(numbers):
    if len(numbers) < 191:
        return None
    sublist = numbers[19:191]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 19:
        return None
    return sorted_sublist[18]