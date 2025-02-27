def find_n_th_smallest_num(numbers):
    if len(numbers) < 191:
        return None
    subset = numbers[19:191]
    subset.sort()
    return subset[18]