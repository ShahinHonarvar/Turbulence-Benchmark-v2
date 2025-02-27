def find_n_th_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    sorted_nums = sorted(numbers[:5])
    return sorted_nums[4]