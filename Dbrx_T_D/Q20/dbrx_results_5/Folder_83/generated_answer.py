def find_n_th_smallest_num(numbers):
    if len(numbers) < 300 - 30 + 1:
        return None
    numbers = sorted(numbers[30:301])
    return numbers[14]