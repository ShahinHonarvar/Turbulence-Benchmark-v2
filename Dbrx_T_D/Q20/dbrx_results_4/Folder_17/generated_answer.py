def find_n_th_smallest_num(numbers):
    if len(numbers) < 85 or len(numbers) > 100:
        return None
    sublist = sorted(numbers[68:86])
    if len(sublist) < 7 or 7 > len(sublist):
        return None
    return sublist[6]