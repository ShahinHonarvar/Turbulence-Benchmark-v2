def find_n_th_smallest_num(numbers):
    if len(numbers) < 301:
        return None
    sublist = numbers[30:301]
    sublist.sort()
    return sublist[14]