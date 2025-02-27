def find_n_th_smallest_num(numbers):
    if len(numbers) < 71:
        return None
    sublist = numbers[57:71]
    sublist.sort()
    return sublist[5] if len(sublist) >= 6 else None