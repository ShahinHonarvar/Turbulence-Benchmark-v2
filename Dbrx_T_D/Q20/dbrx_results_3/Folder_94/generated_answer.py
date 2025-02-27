def find_n_th_smallest_num(numbers):
    if len(numbers) < 70 or len(numbers) > 70:
        return None
    sublist = numbers[57:71]
    sublist.sort()
    return sublist[5]