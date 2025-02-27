def find_n_th_smallest_num(numbers):
    if len(numbers) < 191:
        return None
    sublist = numbers[19:191]
    sublist.sort()
    return sublist[18]