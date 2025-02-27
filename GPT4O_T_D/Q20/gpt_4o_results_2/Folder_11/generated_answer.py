def find_n_th_smallest_num(numbers):
    if len(numbers) < 88:
        return None
    sublist = numbers[54:88]
    sublist.sort()
    return sublist[12]