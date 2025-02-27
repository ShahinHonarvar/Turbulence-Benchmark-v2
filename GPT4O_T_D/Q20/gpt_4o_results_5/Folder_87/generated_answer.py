def find_n_th_smallest_num(numbers):
    if len(numbers) < 67:
        return None
    sublist = numbers[55:67]
    sublist.sort()
    return sublist[5]