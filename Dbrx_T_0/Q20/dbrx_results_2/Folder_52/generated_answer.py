def find_n_th_smallest_num(numbers):
    if len(numbers) < 75 or len(numbers) > 100:
        return None
    sublist = numbers[40:76]
    sublist.sort()
    if len(sublist) < 19:
        return None
    return sublist[18]