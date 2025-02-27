def find_n_th_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sublist = numbers[5:10]
    sublist.sort()
    return sublist[4]