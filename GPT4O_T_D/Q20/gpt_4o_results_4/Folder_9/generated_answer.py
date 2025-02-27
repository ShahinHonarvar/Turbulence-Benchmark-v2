def find_n_th_smallest_num(numbers):
    if len(numbers) < 101:
        return None
    sublist = numbers[10:101]
    sublist.sort()
    return sublist[9] if len(sublist) >= 10 else None