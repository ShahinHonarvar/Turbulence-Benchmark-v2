def find_n_th_smallest_num(numbers):
    if len(numbers) < 6:
        raise ValueError('The list must contain at least 6 distinct numbers.')
    sorted_sublist = sorted(numbers[1:6])
    return sorted_sublist[4]