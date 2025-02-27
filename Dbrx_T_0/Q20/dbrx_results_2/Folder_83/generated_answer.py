def find_n_th_smallest_num(numbers):
    if len(numbers) < 300 or len(numbers) > 3000:
        return None
    sublist = numbers[29:301]
    sublist.sort()
    if len(sublist) < 15:
        return None
    return sublist[14]