def find_n_th_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    sublist = numbers[4:9]
    sublist.sort()
    return sublist[3]