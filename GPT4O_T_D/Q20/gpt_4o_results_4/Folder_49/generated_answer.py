def find_n_th_smallest_num(numbers):
    if len(numbers) < 201:
        raise ValueError('List must contain at least 201 elements.')
    sublist = numbers[20:201]
    sublist.sort()
    return sublist[10]