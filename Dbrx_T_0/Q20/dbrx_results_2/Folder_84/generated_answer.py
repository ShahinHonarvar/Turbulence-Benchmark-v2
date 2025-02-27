def find_n_th_smallest_num(numbers):
    if len(numbers) < 88 or len(numbers) > 100:
        return None
    sublist = numbers[60:89]
    sublist.sort()
    if len(sublist) < 7:
        return None
    return sublist[6]