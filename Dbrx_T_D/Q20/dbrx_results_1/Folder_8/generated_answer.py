def find_n_th_smallest_num(numbers):
    if len(numbers) < 32:
        return None
    target_numbers = numbers[15:32]
    target_numbers.sort()
    if len(target_numbers) < 10:
        return None
    return target_numbers[9]