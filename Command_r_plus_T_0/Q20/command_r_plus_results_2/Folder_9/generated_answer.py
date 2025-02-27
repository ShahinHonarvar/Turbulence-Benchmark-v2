def find_n_th_smallest_num(numbers):
    if len(numbers) < 101:
        return None
    numbers = sorted(numbers[10:101])
    return numbers[9]