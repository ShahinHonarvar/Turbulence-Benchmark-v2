def find_n_th_smallest_num(numbers):
    if len(numbers) < 7:
        raise ValueError('List should have at least 7 elements')
    sorted_nums = sorted(numbers[:7])
    return sorted_nums[6]