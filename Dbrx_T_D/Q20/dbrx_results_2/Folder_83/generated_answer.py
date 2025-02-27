def find_n_th_smallest_num(numbers):
    if len(numbers) < 300:
        return None
    subset = numbers[29:300]
    subset.sort()
    return subset[14]