def find_n_th_smallest_num(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    if len(numbers) < 15 or len(numbers) < 83:
        return None
    return numbers[45:84][14]